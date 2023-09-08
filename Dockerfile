FROM python:alpine

RUN apt-get update

WORKDIR /app

COPY . /app

RUN pip3 install flask

EXPOSE 8080

CMD ["python3", "app.py"]