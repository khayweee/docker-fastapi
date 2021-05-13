FROM python:3.8

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./app/. /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]