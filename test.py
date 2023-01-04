import requests
import time
import sys
#import googletrans


weathercity = input("Météo pour quelle  ville ? : ") # input va nous permettre de saisir le contenu de weathercity
weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+weathercity+'&appid=9db93bdd1a0d2f47617d2c9158a903fa')
url = ('http://api.openweathermap.org/data/2.5/weather?q='+weathercity+'&appid=9db93bdd1a0d2f47617d2c9158a903fa')
# on récupère ci-dessus les données de la requetes web

def spinning_cursor():  # Scimulation d'un temp de hcargement
    while True:
        for cursor in '|/-\\':
            yield cursor  # yield retourne le générateur cursor ( au lieu de stocker on récupère l'info à la volée )
                          # s'éxécute qu'une seule fois

data = weather.json()  # liste en java de weather ( notre requete est stockée dans une liste)

gps = data['coord']  # retourne les coordonnées gps de la station météo
temp = data['main']['temp']
print(gps)
description = data['weather'][0]['description']
weatherprint = "A {}, il fait actuellement {}°C avec {}. Les coordonnés sont {}."
spinner = spinning_cursor()
for _ in range(25):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')

convert = int(temp - 273.15)  # convertir les fahrenheit en celsius

#from googletrans import  Translator
#trad = Translator()
#descr = trad.translate(description, src='en', dest='fr')
print(weatherprint.format(weathercity, convert, description, gps))
