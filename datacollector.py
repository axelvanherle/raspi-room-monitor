import psutil
from prometheus_client import start_http_server, Gauge
import time

cpu_usage = Gauge('cpu_usage', 'CPU Usage', ['core'])
ram_usage = Gauge('ram_usage', 'RAM Usage')
disk_usage = Gauge('disk_usage', 'Disk Usage', ['partition'])
temperature = Gauge('temperature', 'Temperature')
network_upload = Gauge('network_upload', 'Network Upload Speed', ['interface'])
network_download = Gauge('network_download', 'Network Download Speed', ['interface'])

def collect_system_metrics():
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpu_usage.labels(core=f'core_{i}').set(percentage)

    ram = psutil.virtual_memory()
    ram_usage.set(ram.percent)

    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        disk_usage.labels(partition=partition.device).set(usage.percent)

    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temp = float(file.read()) / 1000
            temperature.set(temp)
    except FileNotFoundError:
        print("Temperature sensor not found")

    for interface_name, interface_stats in psutil.net_io_counters(pernic=True).items():
        if interface_name == 'wlan0':  # Replace with your wireless interface name if different
            network_upload.labels(interface=interface_name).set(interface_stats.bytes_sent)
            network_download.labels(interface=interface_name).set(interface_stats.bytes_recv)

start_http_server(8000)

while True:
    collect_system_metrics()
    time.sleep(60)
