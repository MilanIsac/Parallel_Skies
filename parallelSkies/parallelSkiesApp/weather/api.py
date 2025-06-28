import requests
import os

def get_weather_data(city):
    api_key = os.getenv('WEATHER_API_KEY')
    if not api_key:
        return {'city': city, 'error': 'API key not set'}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            return {'city': city, 'error': data.get('message', 'Error')}
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'].capitalize(),
            'icon': data['weather'][0]['icon'],
            'feels_like': data['main']['feels_like'],
            'wind_speed': data['wind']['speed'],
        }
    except Exception as e:
        return {'city': city, 'error': 'Failed to fetch data'}
