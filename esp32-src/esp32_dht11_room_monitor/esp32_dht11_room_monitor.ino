#include <WiFi.h>
#include <WebServer.h>
#include <DHT.h>
#include "credentials.h"

#define DHTPIN 15

DHT dht(DHTPIN, DHT11);
WebServer server(80);

void setup()
{
  Serial.begin(9600);
  dht.begin();
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  server.on("/esp32_metrics", HTTP_GET, handleMetrics);
  server.begin();
}

void loop()
{
  server.handleClient();
}

void handleMetrics()
{
  float humidity = dht.readHumidity();
  float temperatureC = dht.readTemperature();

  if (isnan(humidity) || isnan(temperatureC))
  {
    server.send(500, "text/plain", "Sensor error");
    return;
  }

  String response = "# HELP esp32_temperature_celsius Current temperature in Celsius\n";
  response += "# TYPE esp32_temperature_celsius gauge\n";
  response += "esp32_temperature_celsius " + String(temperatureC) + "\n";
  response += "# HELP esp32_humidity_percent Current humidity in percent\n";
  response += "# TYPE esp32_humidity_percent gauge\n";
  response += "esp32_humidity_percent " + String(humidity) + "\n";

  server.send(200, "text/plain", response);
}
