FROM python:3.6.5

RUN mkdir -p /app
WORKDIR /app

CMD ["python", "/app/main.py"]