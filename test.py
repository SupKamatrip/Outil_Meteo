# python_test.py
import requests

api_key = "9db93bdd1a0d2f47617d2c9158a903fa"  # Enter the API key you got from the OpenWeatherMap website
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]

    current_temperature = y["temp"]
    z = x["weather"]

    weather_description = z[0]["description"]

    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n description = " +
                    str(weather_description))

else:
    print(" City Not Found ")