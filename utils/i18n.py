from typing import Dict

class I18n:
    def __init__(self, lang: str = "en"):
        self.lang = lang
        self.translations: Dict[str, Dict[str, str]] = {
            "en": {
                "title": "PDF Translator",
                "upload_label": "Upload PDF here",
                "translate_btn": "Translate",
                "translated_label": "Translated PDF",
                "images_label": "Translated PDF Images",
                "error_msg": "An error occurred: {}",
                "done_msg": "Done.",
                "translating_msg": "Translating {}...",
                "saved_msg": "Converted PDF saved to {}",
                "input_error": "Input file must be a PDF or directory: {}",
                "empty_dir_error": "Input directory is empty: {}",
                "path_error": "Input path must be a file or directory: {}",
                "lang_label": "Target Language",
            },
            "ja": {
                "title": "PDF Translator",
                "upload_label": "ここにPDFをアップロード",
                "translate_btn": "翻訳",
                "translated_label": "翻訳されたPDF",
                "images_label": "翻訳されたPDFの画像",
                "error_msg": "エラーが発生しました: {}",
                "done_msg": "完了。",
                "translating_msg": "{} を翻訳中...",
                "saved_msg": "変換されたPDFは {} に保存されました",
                "input_error": "入力ファイルはPDFまたはディレクトリである必要があります: {}",
                "empty_dir_error": "入力ディレクトリが空です: {}",
                "path_error": "入力パスはファイルまたはディレクトリである必要があります: {}",
                "lang_label": "翻訳先の言語",
            },
            "zh": {
                "title": "PDF 翻译器",
                "upload_label": "在此上传 PDF",
                "translate_btn": "翻译",
                "translated_label": "已翻译的 PDF",
                "images_label": "已翻译 PDF 的图像",
                "error_msg": "发生错误: {}",
                "done_msg": "完成。",
                "translating_msg": "正在翻译 {}...",
                "saved_msg": "已转换的 PDF 保存至 {}",
                "input_error": "输入文件必须是 PDF 或目录: {}",
                "empty_dir_error": "输入目录为空: {}",
                "path_error": "输入 path 必须是文件或目录: {}",
                "lang_label": "目标语言",
            }
        }

    def get(self, key: str, *args) -> str:
        """Get translated string."""
        lang_dict = self.translations.get(self.lang, self.translations["en"])
        text = lang_dict.get(key, key)
        if args:
            return text.format(*args)
        return text

    def set_lang(self, lang: str):
        if lang in self.translations:
            self.lang = lang

i18n = I18n()
