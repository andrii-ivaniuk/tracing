FROM python:3.8-buster

RUN mkdir -p /opt/app

RUN apt-get update && apt-get install python3-psycopg2 -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app

RUN pip install uvicorn

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./app ./app

EXPOSE 8000

CMD uvicorn --host=0.0.0.0 app.main:app --port 8000