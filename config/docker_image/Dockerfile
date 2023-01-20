# syntax=docker/dockerfile:1

FROM python:3

RUN apt-get update && apt-get install -y git

WORKDIR /code

RUN git clone https://github.com/rvasconcelossilva/data-mesh.git

RUN pip install pipenv

WORKDIR /data-mesh

RUN pipenv install

RUN uvicorn --help

#CMD ["python3", "uvicorn", "main:app", "--reload", "--app-dir ./tools/dpt_api"]

EXPOSE 8000