# data-processor/Dockerfile
FROM python:3.8-slim

# WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install paho-mqtt

COPY . .

CMD ["python", "main.py"]
