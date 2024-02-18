import Adafruit_DHT
import time

# Sensor type
DHT_SENSOR = Adafruit_DHT.DHT22

DHT_PIN = 21

def read_dht22():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from sensor")

def main():
    while True:
        read_dht22()
        time.sleep(2)  # Delay between readings, set to 2 seconds

if __name__ == "__main__":
    main()
