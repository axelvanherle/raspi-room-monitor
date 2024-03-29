import smbus
from prometheus_client import Gauge

bh1750_addr = 0x23
bus = smbus.SMBus(1)

light_intensity_gauge = Gauge('room_light_intensity_lux', 'Room Light Intensity in Lux')

def collect_bh1750_metrics():
    data = bus.read_i2c_block_data(bh1750_addr, 0x11)
    light_level = (data[1] + (256 * data[0])) / 1.2
    light_intensity_gauge.set(light_level)
