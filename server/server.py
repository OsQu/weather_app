from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

import requests

URL = "https://api.open-meteo.com/v1/forecast"

"""
Weather codes:
+------------+------------------------------------------------+
| Code       | Description                                    |
+------------+------------------------------------------------+
| 0          | Clear sky                                      |
| 1, 2, 3    | Mainly clear, partly cloudy, and overcast      |
| 45, 48     | Fog and depositing rime fog                    |
| 51, 53, 55 | Drizzle: Light, moderate, and dense intensity  |
| 56, 57     | Freezing Drizzle: Light and dense intensity    |
| 61, 63, 65 | Rain: Slight, moderate and heavy intensity     |
| 66, 67     | Freezing Rain: Light and heavy intensity       |
| 71, 73, 75 | Snow fall: Slight, moderate, and heavy         |
| 77         | Snow grains                                    |
| 80, 81, 82 | Rain showers: Slight, moderate, and violent    |
| 85, 86     | Snow showers slight and heavy                  |
| 95         | Thunderstorm: Slight or moderate               |
| 96, 99     | Thunderstorm with slight and heavy hail        |
+------------+------------------------------------------------+
"""


def get_weather_data():
    # Set coordinates for weather data (example: New York City)
    latitude = 40.7128
    longitude = -74.0060

    # Configure parameters for the API request
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "weather_code,temperature,precipitation",
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()  # Raise an exception for bad status codes
    weather_data = response.json()

    return weather_data["current"]


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def handle_forecast(self):
        weather_data = get_weather_data()

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(weather_data).encode())

    def handle_default(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b'404 Not Found')

    def do_GET(self):
        if self.path == '/forecast':
            self.handle_forecast()
        else:
            self.handle_default()


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    port = int(os.environ.get('PORT', 3000))
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
