# syntax=docker/dockerfile:1

FROM python:3.9

RUN apt-get update && apt-get install -y git && apt install zsh -y

WORKDIR /code

RUN git clone https://github.com/rvasconcelossilva/data-mesh.git

RUN pip install pipenv

WORKDIR /code/data-mesh

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system --deploy --ignore-pipfile

RUN sh -c "$(wget -O- https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN cd /code/data-mesh

CMD ["uvicorn", "tools.dpt_api.main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000