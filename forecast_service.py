# app_weather_forecast.py
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

OPENWEATHERMAP_API_KEY = '3656096e864188f8e7bfaf3be3577e51'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather_forecast')
def get_weather_forecast():
    location = request.args.get('location')

    if not location:
        return render_template('error.html', message="Please provide location parameter.")

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={OPENWEATHERMAP_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return render_template('error.html', message=f"Failed to fetch weather forecast data. Error: {data['message']}")

    # Extract weather forecast data for the next 5 days
    forecast_data = []
    for entry in data['list']:
        forecast_time = entry['dt_txt']
        weather_description = entry['weather'][0]['description']
        temperature_kelvin = entry['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        forecast_data.append({'time': forecast_time, 'weather': weather_description, 'temperature': temperature_celsius})

    return render_template('weather_forecast.html', location=location, forecast_data=forecast_data)

if __name__ == "__main__":
    app.run(debug=True, port=5003)
