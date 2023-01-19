# syntax=docker/dockerfile:1

FROM python:3

ARG gh_token
ENV env_name $gh_token

WORKDIR /code

RUN brew install gh

RUN gh repo clone rvasconcelossilva/data-mesh

WORKDIR /data-mesh

RUN pipenv install