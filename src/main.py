import time
import logging
from prometheus_client import start_http_server
from system_metrics import collect_system_metrics
from openweather_current_metrics import send_openweather_current_api_req
from dht22_metrics import collect_dht22_metrics
from bh1750_metrics import collect_bh1750_metrics

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

try:
    start_http_server(8000)
    logging.info("HTTP server started on port 8000")
except Exception as e:
    logging.error(f"Failed to start HTTP server: {e}")
    exit(1)

while True:
    try:
        collect_system_metrics()
        logging.info("Collected system_metrics.")
    except Exception as e:
        logging.error(f"Error collecting system metrics: {e}")
        continue

    try:
        send_openweather_current_api_req()
        logging.info("Collected current_openweather_api_data.")
    except Exception as e:
        logging.error(f"Error fetching current_weather data: {e}")
        continue

    try:
        collect_dht22_metrics()
        logging.info("Collected dht22_metrics")
    except Exception as e:
        logging.error(f"Error collecting dht22_metrics: {e}")
        continue

    try:
        collect_bh1750_metrics()
        logging.info("Collected bh1750_metrics")
    except Exception as e:
        logging.error(f"Error collecting bh1750_metrics: {e}")
        continue

    time.sleep(60)
