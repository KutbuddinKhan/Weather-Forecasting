# Weather Forecast

This is a simple Python script that fetches weather data for a given city using the OpenWeatherMap API and displays the temperature and other weather information.

## Prerequisites

To run this script, you need the following:

- Python 3.x installed on your system.
- An API key from OpenWeatherMap. You can sign up for a free API key at [OpenWeatherMap API](https://openweathermap.org/api).

## Installation

1. Clone the repository or download the script file.
   ```shell
   git clone https://github.com/your-username/weather-forecast.git
   ```
2. Install the required dependencies.
   ```shell
      pip install requests
   ```
3. Usage
   Open a terminal or command prompt and navigate to the project directory.
   Run the script.
   ```shell
      python main.py
   ```
   Enter the name of the city for which you want to fetch the weather forecast when prompted.
   The script will retrieve the weather data from OpenWeatherMap and display the temperature in Celsius, along with other weather information

## Architecture Flow

The architectural flow of the Weather Forecast script can be described as follows:

User initiates the script by running main.py from the command line.

The script prompts the user to enter the name of the city for which they want to fetch the weather forecast.

The user input is received and stored in a variable.

The script makes a request to the OpenWeatherMap API, passing the city name and API key as parameters.

The API response is received, and the script parses the JSON data to extract the relevant weather information.

The temperature is converted from Fahrenheit to Celsius using the provided formula.

The script displays the weather data, including the city name, temperature in Celsius, weather description, and wind speed.

The execution of the script ends.

## Using Github Copilot

This project utilizes GitHub Copilot, an AI-powered coding assistant. Here are a few scenarios where GitHub Copilot can be helpful:

API Integration: GitHub Copilot assisted us in integrating external APIs, like OpenWeatherMap, by suggesting the necessary code snippets for making requests and handling responses.

![ScreenShot of Copilot Recommendation](Screenshots/ss1.jpeg)
Here you can see that github copilot is suggesting me the code snippet for integrating params to fetch data from API

Helping in Coversion of Temperatures:
![ScreenShot of Copilot Recommendation](Screenshots/ss2.jpeg)
![ScreenShot of Copilot Recommendation](Screenshots/ss3.jpeg)
![ScreenShot of Copilot Recommendation](Screenshots/ss4.jpeg)

Helping in Exception Handling:
![ScreenShot of Copilot Recommendation](Screenshots/ss5.jpeg)
![ScreenShot of Copilot Recommendation](Screenshots/ss6.jpeg)

## Final Output

![ScreenShot of Final OutPut](Screenshots/Final%20Output.jpeg)
