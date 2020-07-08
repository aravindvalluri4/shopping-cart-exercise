From python:3.8.3-slim-buster

ADD app /app

WORKDIR /app

RUN python -m unittest -v

CMD ["python", "main.py"]


