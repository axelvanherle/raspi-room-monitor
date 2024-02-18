import adafruit_dht
from prometheus_client import Gauge

dht_sens = Adafruit_DHT.DHT22
dht_pin = 21

temperature_gauge = Gauge('room_temperature_celsius', 'Room Temperature in Celsius')
humidity_gauge = Gauge('room_humidity_percentage', 'Room Humidity in Percentage')

def collect_dht22_metrics():
    humidity, temperature = Adafruit_DHT.read_retry(dht_sens, dht_pin)
    temperature_gauge.set(temperature)
    humidity_gauge.set(humidity)
    
