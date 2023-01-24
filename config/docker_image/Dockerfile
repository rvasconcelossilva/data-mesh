# syntax=docker/dockerfile:1

FROM python:3.9

RUN apt-get update && apt-get install -y git

WORKDIR /code

RUN git clone https://github.com/rvasconcelossilva/data-mesh.git

RUN pip install pipenv

WORKDIR /code/data-mesh

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system --deploy --ignore-pipfile

CMD ["uvicorn", "tools.dpt_api.main:app", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 80

#RUN pip install --upgrade pip

#RUN pip install -r requirements.txt

#RUN ["uvicorn", "main:app", "--reload", "--app-dir ./tools/dpt_api"]