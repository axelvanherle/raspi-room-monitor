# raspi-room-monitor

Turn your raspberry pi into a monitoring device where you collect metrics to visualize what's going on in your room.

*This project is known to work on a raspberry pi 3b+, your mileage may vary.*

A blogpost has been made about this which you can find [here](https://www.axelvanherle.xyz/blog/2024-03-12_raspiroommonitor/).

## Demo

| | |
|---|---|
| ![db4](https://github.com/axelvanherle/raspi-room-monitor/assets/94362354/163fe000-c714-477c-9bd4-cfb336aad103) | ![db3](https://github.com/axelvanherle/raspi-room-monitor/assets/94362354/036ffaab-6d35-4c2e-95eb-36893f8c0976) |
| ![db2](https://github.com/axelvanherle/raspi-room-monitor/assets/94362354/bbe738ab-6c6e-45f5-8019-f4e9cb19f95f) | ![db1](https://github.com/axelvanherle/raspi-room-monitor/assets/94362354/91cad06f-474f-401e-83f3-095f11af71eb) |

## Howto
### My way
If you want to exactly replicate my stack this is what you're gonna need;
- raspberry pi (i used the 3b+, this project is known to work on a raspberry pi 3b+, your mileage may vary)
- esp32 (i used a esp32s)
- dht11 sensor
- dht22 sensor
- bh1750 sensor

Get started by installing docker on your pi, you can find out how to do that [here](https://docs.docker.com/engine/install/debian/).
After that you're gonna want to make sure i2c is enabled on your pi, you can find out more about that [here](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c).

Let's start with connecting everything to the pi.
- Power each connector by hooking it up to 3.3V and GND. I don't include a diagram because the package these ship with is not universal.
- The signal pin from the DHT22 goes to GPIO 21.
- The BH1750 interfaces via I2C, so hook that up correctly with your pi. Once again the pins are different for each pi, so you're gonna have to do a quick google.

Next we're gonna connect the DHT11 to the ESP32.
- Power it by hooking it up to 3.3V and GND. I don't include a diagram because the package these ship with is not universal.
- The signal pin from the DHT22 goes to GPIO 15.

Once you've got it all connected we're gonna move to the software side of things. You don't need to chance much here, only the `.env` file. If you're not sure when or how to do this, that's explained later.
- Enter your OpenWeatherAPI key. You can find out how to get one [here](https://openweathermap.org/appid).
- Find the LAT and LON of your city, or the city you plan on tracking.
- Then decide if you feel like using metric or imperial.
- Enter your WiFi credentials in `esp32-src/esp32_dht11_room_monitor/credentials.h`

An example configuration might look like this for the `.env` file;
```
OPENWEATHER_API_KEY=1234567890abcdef1234567890abcdef
LAT=34.0522
LON=-118.2437
UNITS=metric
```
And like this for the `credentials.h` file;
```
// credentials.h
const char* ssid = "ExampleNetwork123";
const char* password = "VerySecurePassword456";
```

Now that we've got everything plugged in and setup it's time to get us up and running.

Firstly you're gonna want to flash the ESP32 using the `esp32-src/esp32_dht11_room_monitor/esp32_dht11_room_monitor.ino` firware. Install the libraries if you don't have them.

Once flashed you're gonna want to get a shell into the rpi. You can get one over UART, or setting up SSH.

Once you have a shell you can copy and paste these commands;
- `git clone https://github.com/axelvanherle/raspi-room-monitor.git`
- `cd raspi-room-monitor`
- At this point you need to modify the .env file like i talked about previously. Use your preffered text editor
- `docker compose up -d`
- That's it, now you can find your dashboard by going to `<rpi ip addr>:3000` in your browser.

### Your way

- ![GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmR4N3Vlc3Q0a3h1M2lkanBhOHB6dm5tdGc5OG8zdHQ1dndvbG53aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YrSc8Vyn355xs6Qxxe/giphy.gif)
- [My blogpost](https://www.axelvanherle.xyz/blog/2024-03-12_raspiroommonitor/) goes into some technical detail.
