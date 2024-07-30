from flask import Flask, render_template, request
import requests
import math

app = Flask(__name__)

# API key and URL
api_key = "30d4741c779ba94c470ca1f63045390a"
url = "http://api.openweathermap.org/data/2.5/weather"


# Function to fetch the weather data
def get_weather_data(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# Function to convert the temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(temp_feh):
    temp_cel = (temp_feh - 32) * 5/9
    return math.ceil(temp_cel)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        try:
            data = get_weather_data(city)
            temp_feh = data['main']['temp']
            temp_cel = fahrenheit_to_celsius(temp_feh)
            weather_data = {
                "city": data['name'],
                "temperature": temp_cel,
                "description": data['weather'][0]['description'],
                "wind_speed": data['wind']['speed']
            }
        except requests.exceptions.HTTPError as err:
            error = f"HTTP Error: {err}"
        except requests.exceptions.RequestException as err:
            error = f"Request Error: {err}"
        except (KeyError, IndexError) as err:
            error = f"Data Error: {err}"
        except Exception as err:
            error = str(err)

    return render_template('index.html', weather_data=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
