FROM arm32v7/python
WORKDIR /usr/src/app
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libgpiod2 build-essential
COPY src/*.py ./
RUN pip install prometheus_client psutil requests Adafruit_DHT
CMD ["python", "./main.py"]
