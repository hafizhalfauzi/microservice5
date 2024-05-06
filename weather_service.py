# app_weather_by_location.py
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

OPENWEATHERMAP_API_KEY = '3656096e864188f8e7bfaf3be3577e51'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather')
def get_weather():  
    location = request.args.get('location')
    if not location:
        return render_template('error.html', message="Please provide location parameter.")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHERMAP_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return render_template('error.html', message=f"Failed to fetch weather data. Error: {data['message']}")

    weather_description = data['weather'][0]['description']
    temperature_kelvin = data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15

    return render_template('weather.html', location=location, weather=weather_description, temperature=temperature_celsius)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
