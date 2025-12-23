NAME=pdf-translator
TAG=0.1.0
PROJECT_DIRECTORY=$(shell pwd)/..

build:
	docker build --build-arg http_proxy=http://192.168.3.122:7890 \
        --build-arg https_proxy=http://192.168.3.122:7890 \
        --build-arg no_proxy=localhost,127.0.0.1,.local -t ${NAME}:${TAG} .

run:
	docker run -it \
		--runtime=nvidia \
		--name pdf-translator \
		-v ${PROJECT_DIRECTORY}:/app \
		--gpus all \
		-d --restart=always \
		-p 8765:8765 \
		-p 8288:8288 \
		${NAME}:${TAG} /bin/bash -c "chmod +x /app/docker/start.sh && /app/docker/start.sh"

run-bash:
	docker run -it \
		--runtime=nvidia \
		--name pdf-translator \
		-v ${PROJECT_DIRECTORY}:/app \
		--gpus all \
		-d --restart=always \
		-p 8765:8765 \
		-p 8288:8288 \
		${NAME}:${TAG} /bin/bash

translate:
	@cd ${PROJECT_DIRECTORY} && \
		python3 cli.py -i ${INPUT}
