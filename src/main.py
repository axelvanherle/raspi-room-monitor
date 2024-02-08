import time
import logging
from prometheus_client import start_http_server
from system_metrics import collect_system_metrics
from weather_data import send_openweather_api_req

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
    except Exception as e:
        logging.error(f"Error collecting system metrics: {e}")
        continue

    try:
        send_openweather_api_req()
    except Exception as e:
        logging.error(f"Error fetching weather data: {e}")
        continue

    time.sleep(60)
