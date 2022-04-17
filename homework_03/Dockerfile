FROM python:3.9-buster

'''
Что бы запустить нужно выполнить команду:
docker run -it -p 8000:8000 app
'''

ENV PYTHONUNBUFFERED=1

WORKDIR /

RUN pip install poetry==1.1.13
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY homework_03 .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]
