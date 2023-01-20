# syntax=docker/dockerfile:1

FROM python:3

RUN apt-get update && apt-get install -y git

WORKDIR /code

RUN git clone https://github.com/rvasconcelossilva/data-mesh.git

RUN pip install pipenv

WORKDIR /data-mesh

RUN uvicorn --app-dir tool/dpt_api main:app --reload