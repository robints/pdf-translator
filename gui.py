from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

import gradio as gr
import requests
from pdf2image import convert_from_path
from PIL import Image

from utils.i18n import i18n

TRANSLATE_URL = "http://localhost:8765/translate_pdf/"
CLEAR_TEMP_URL = "http://localhost:8765/clear_temp_dir/"


def translate_request(
    file: Any, target_lang_name: str
) -> tuple[Path, list[Image.Image]]:
    """Sends a POST request to the translator server to translate a PDF.

    Parameters
    ----------
    file : Any
        the PDF to be translated.
    target_lang_name : str
        The selected target language name (e.g., "Japanese", "Chinese").

    Returns
    -------
    tuple[Path, list[Image.Image]]
        Path to the translated PDF and a list of images of the
        translated PDF.
    """
    lang_map = {"English": "en", "Japanese": "ja", "Chinese": "zh"}
    target_lang = lang_map.get(target_lang_name, "ja")

    response = requests.post(
        TRANSLATE_URL,
        files={"input_pdf": open(file.name, "rb")},
        params={"target_lang": target_lang},
    )

    if response.status_code == 200:
        with open(Path(temp_dir) / "translated.pdf", "wb") as f:
            f.write(response.content)

        images = convert_from_path(Path(temp_dir) / "translated.pdf")

        requests.get(CLEAR_TEMP_URL)
        return str(Path(temp_dir) / "translated.pdf"), images
    else:
        print(f"An error occurred: {response.status_code}")


def update_ui(lang_name: str):
    lang_map = {"English": "en", "Japanese": "ja", "Chinese": "zh"}
    code = lang_map.get(lang_name, "ja")
    i18n.set_lang(code)
    return [
        gr.Markdown(value=f"## {i18n.get('title')}"),
        gr.File(label=i18n.get("upload_label")),
        gr.Button(value=i18n.get("translate_btn")),
        gr.File(label=i18n.get("translated_label")),
        gr.Gallery(label=i18n.get("images_label")),
    ]


if __name__ == "__main__":
    global temp_dir
    # Set default language to Japanese to match original behavior
    i18n.set_lang("ja")

    with TemporaryDirectory() as temp_dir:
        with gr.Blocks(theme="Soft") as demo:
            with gr.Column():
                lang_dropdown = gr.Dropdown(
                    choices=["Japanese", "Chinese", "English"],
                    value="Japanese",
                    label=i18n.get("lang_label"),
                )
                title = gr.Markdown(f"## {i18n.get('title')}")
                file = gr.File(label=i18n.get("upload_label"))
                btn = gr.Button(value=i18n.get("translate_btn"))
                translated_file = gr.File(
                    label=i18n.get("translated_label"), file_types=[".pdf"]
                )
                pdf_images = gr.Gallery(label=i18n.get("images_label"))

                btn.click(
                    translate_request,
                    inputs=[file, lang_dropdown],
                    outputs=[translated_file, pdf_images],
                )

                lang_dropdown.change(
                    update_ui,
                    inputs=[lang_dropdown],
                    outputs=[title, file, btn, translated_file, pdf_images],
                )

        demo.queue().launch(server_name="0.0.0.0", server_port=8288)
