import requests
from prometheus_client import Gauge
from config import APIKEY, LAT, LON, UNITS

url = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={APIKEY}&units={UNITS}'
# from main
temperature_gauge = Gauge('weather_temperature', 'Temperature')
feels_like_gauge = Gauge('weather_feels_like', 'Feels Like Temperature')
pressure_gauge = Gauge('weather_pressure', 'Pressure')
humidity_gauge = Gauge('weather_humidity', 'Humidity')
# wind data
wind_speed_gauge = Gauge('weather_wind_speed', 'Wind Speed')
wind_gust_gauge = Gauge('weather_wind_gust', 'Wind Gust')
# cloud data
cloudiness_gauge = Gauge('weather_cloudiness', 'Cloudiness')
# rain data
rain_1h_gauge = Gauge('weather_rain_1h', 'Rain Volume for last hour')
# sys data
sunrise_gauge = Gauge('weather_sunrise', 'Sunrise Time')
sunset_gauge = Gauge('weather_sunset', 'Sunset Time')

def send_openweather_current_api_req():
    recvbuffer = requests.get(url)
    if recvbuffer.status_code == 200:
        data = recvbuffer.json()
        # main data
        temperature_gauge.set(data['main']['temp'])
        feels_like_gauge.set(data['main']['feels_like'])
        pressure_gauge.set(data['main']['pressure'])
        humidity_gauge.set(data['main']['humidity'])
        # wind data
        wind_speed_gauge.set(data['wind']['speed'])
        wind_gust_gauge.set(data['wind'].get('gust', 0))
        # clouds
        cloudiness_gauge.set(data['clouds']['all'])
        # rain data
        rain_1h_gauge.set(data.get('rain', {}).get('1h', 0))
        # xys data
        sunrise_gauge.set(data['sys']['sunrise'])
        sunset_gauge.set(data['sys']['sunset'])
    else:
        print('Error fetching weather data')
