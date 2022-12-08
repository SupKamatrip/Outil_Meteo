import requests
import time
import sys
#import googletrans


weathercity = input("Météo pour quelle  ville ? : ")
weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+weathercity+'&appid=9db93bdd1a0d2f47617d2c9158a903fa')
url = ('http://api.openweathermap.org/data/2.5/weather?q='+weathercity+'&appid=9db93bdd1a0d2f47617d2c9158a903fa')




def spinning_cursor():  # Scimulation d'un temp de hcargement
    while True:
        for cursor in '|/-\\':
            yield cursor


data = weather.json()

temp = data['main']['temp']
print(temp)
description = data['weather'][0]['description']
weatherprint = "Dans {}, il fait actuellement {}°C avec {}."
spinner = spinning_cursor()
for _ in range(25):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')

convert = int(temp - 273.15)

#from googletrans import  Translator
#trad = Translator()
#descr = trad.translate(description, src='en', dest='fr')
print(weatherprint.format(weathercity, convert, description))
