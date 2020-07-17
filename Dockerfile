FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y build-essential cmake python3.7-dev

RUN pip3 install requests

WORKDIR /usr/src/app

COPY . ./

CMD ["python3", "main.py"]
