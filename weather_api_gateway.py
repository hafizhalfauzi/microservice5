from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

WEATHER_SERVICE_URL = 'http://localhost:5002'
FORECAST_SERVICE_URL = 'http://localhost:5003'
COORDINATES_SERVICE_URL = 'http://localhost:5000'
POSTAL_CODE_SERVICE_URL = 'http://localhost:5001'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Please provide location parameter.'}), 400
    
    # Call Weather Service
    response = requests.get(f"{WEATHER_SERVICE_URL}/weather", params={'location': location})
    return response.content, response.status_code

@app.route('/weather_forecast')
def get_weather_forecast():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Please provide location parameter.'}), 400
    
    # Call Forecast Service
    response = requests.get(f"{FORECAST_SERVICE_URL}/weather_forecast", params={'location': location})
    return response.content, response.status_code

@app.route('/weather_by_coordinates')
def get_weather_by_coordinates():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    if not latitude or not longitude:
        return jsonify({'error': 'Please provide latitude and longitude parameters.'}), 400
    
    # Call Coordinates Service
    response = requests.get(f"{COORDINATES_SERVICE_URL}/weather_by_coordinates", params={'lat': latitude, 'lon': longitude})
    return response.content, response.status_code

@app.route('/weather_by_postal_code')
def get_weather_by_postal_code():
    postal_code = request.args.get('postal_code')
    if not postal_code:
        return jsonify({'error': 'Please provide postal code parameter.'}), 400
    
    # Call Postal Code Service
    response = requests.get(f"{POSTAL_CODE_SERVICE_URL}/weather_by_postal_code", params={'postal_code': postal_code})
    return response.content, response.status_code

if __name__ == "__main__":
    app.run(debug=True, port=5004)
