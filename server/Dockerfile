FROM python:3.8-alpine

WORKDIR /code

COPY . /code

RUN pip3 install -r requirements.txt

# ,"--ssl-keyfile","server.key","--ssl-certfile","server.crt"
CMD ["uvicorn","server:app","--reload","--host","0.0.0.0"]