# mqtt-client/Dockerfile
FROM python:3.9

WORKDIR ./app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "C:\Users\dawid\OneDrive\Pulpit\projektDocker\mqtt-client\app\main.py"]
