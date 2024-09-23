FROM python:3.12-alpine AS builder

COPY requirements.txt ./

RUN --mount=type=cache,target=./.pip-cache pip install --cache-dir ./.pip-cache -r requirements.txt

COPY ./app ./app

ENTRYPOINT [ "python" , "./app/main.py" ]