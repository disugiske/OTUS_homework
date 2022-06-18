FROM tiangolo/uwsgi-nginx-flask:python3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app-api-flask /app
