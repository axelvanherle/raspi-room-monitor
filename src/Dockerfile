FROM python:3.8-slim
WORKDIR /usr/src/app
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libgpiod2 build-essential
COPY src/*.py ./
RUN pip install prometheus_client psutil requests adafruit-circuitpython-dht
CMD ["python", "./main.py"]
