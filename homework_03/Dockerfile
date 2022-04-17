FROM python:3.9-buster

WORKDIR /

RUN pip install poetry==1.1.13
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install
