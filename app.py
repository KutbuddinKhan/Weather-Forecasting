from flask import Flask, render_template, request, redirect, url_for
import requests
import math
from datetime import datetime
import json
import sqlite3

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
    temp_cel = (temp_feh - 32) * 5 / 9
    return math.ceil(temp_cel)

# Custom Jinja filter for formatting datetime


@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d %H:%M:%S'):
    return datetime.fromtimestamp(value).strftime(format)

# Function to insert a city name into the database


# def insert_city(city):
#     connection = sqlite3.connect('weather_city.db')
#     cursor = connection.cursor()
#     cursor.execute('''
#         INSERT INTO cities (city_name)
#                    VALUES (?)
#     ''',
#                    (city,))
#     connection.commit()
#     connection.close()

def insert_city(city):
    connection = sqlite3.connect('weather_city.db')
    cursor = connection.cursor()
    try:
        cursor.execute('''
            INSERT INTO cities (city_name)
            VALUES (?)
        ''', (city,))
        connection.commit()
        print(f"Inserted city: {city}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        connection.close()



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
                "wind_speed": data['wind']['speed'],
                "humidity": data['main']['humidity'],
                "pressure": data['main']['pressure'],
                "sunrise": data['sys']['sunrise'],
                "sunset": data['sys']['sunset']
            }
            insert_city(city)
        except requests.exceptions.HTTPError as err:
            error = f"HTTP Error: {err}"
        except requests.exceptions.RequestException as err:
            error = f"Request Error: {err}"
        except (KeyError, IndexError) as err:
            error = f"Data Error: {err}"
        except Exception as err:
            error = str(err)

    return render_template('index.html', weather_data=weather_data, error=error)


@app.route('/visualize')
def visualize():
    weather_data = request.args.get('weather_data', None)
    if weather_data:
        weather_data = json.loads(weather_data)  # Convert JSON string to dict
    return render_template('visualize.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
