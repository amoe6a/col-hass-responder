FROM python:3.8-slim-buster

WORKDIR /col-has-responder

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "app.py"]