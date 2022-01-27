FROM python:3.9.9

WORKDIR /app

COPY . .

CMD ["python", "main.py"]