import requests
from prometheus_client import Gauge
from config import APIKEY, LAT, LON, UNITS

url = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={APIKEY}&units={UNITS}'
# from main
temperature_gauge = Gauge('weather_temperature', 'Temperature')
feels_like_gauge = Gauge('weather_feels_like', 'Feels Like Temperature')
temp_min_gauge = Gauge('weather_temp_min', 'Minimum Temperature')
temp_max_gauge = Gauge('weather_temp_max', 'Maximum Temperature')
pressure_gauge = Gauge('weather_pressure', 'Pressure')
humidity_gauge = Gauge('weather_humidity', 'Humidity')
sea_level_pressure_gauge = Gauge('weather_sea_level_pressure', 'Sea Level Pressure')
ground_level_pressure_gauge = Gauge('weather_ground_level_pressure', 'Ground Level Pressure')
# wind data
wind_speed_gauge = Gauge('weather_wind_speed', 'Wind Speed')
wind_deg_gauge = Gauge('weather_wind_deg', 'Wind Degree')
wind_gust_gauge = Gauge('weather_wind_gust', 'Wind Gust')
# cloud data
cloudiness_gauge = Gauge('weather_cloudiness', 'Cloudiness')
# rain data
rain_1h_gauge = Gauge('weather_rain_1h', 'Rain Volume for last hour')
# sys data
sunrise_gauge = Gauge('weather_sunrise', 'Sunrise Time')
sunset_gauge = Gauge('weather_sunset', 'Sunset Time')

def send_openweather_api_req():
    recvbuffer = requests.get(url)
    if recvbuffer.status_code == 200:
        data = recvbuffer.json()
        # main data
        temperature_gauge.set(data['main']['temp'])
        feels_like_gauge.set(data['main']['feels_like'])
        temp_min_gauge.set(data['main']['temp_min'])
        temp_max_gauge.set(data['main']['temp_max'])
        pressure_gauge.set(data['main']['pressure'])
        humidity_gauge.set(data['main']['humidity'])
        sea_level_pressure_gauge.set(data['main'].get('sea_level', 0))
        ground_level_pressure_gauge.set(data['main'].get('grnd_level', 0))
        # wind data
        wind_speed_gauge.set(data['wind']['speed'])
        wind_deg_gauge.set(data['wind'].get('deg', 0))
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

