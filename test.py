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
temp = data['main']['temp'] # retourne les données contenus dans main et temp de la requête web
description = data['weather'][0]['description']

weatherprint = "A {}, il fait actuellement {}°C avec {}. Les coordonnées GPS de la station météo sont {}."

spinner = spinning_cursor()  # on fait appel à notre fonction précédemment définie
for _ in range(25):  # le _ permet d'ignorer l'itération, peut importe là ou ca en est la boucle est lancée
    sys.stdout.write(next(spinner))  # nous permet d'écrire/afficher le logo de chargement
    sys.stdout.flush() # Affiche immediatement le curseur plutot que d'attendre que le tampon soit plein
    time.sleep(0.1) # mets en pause 0.1 seconde a chaque itération dans la boucle for
    sys.stdout.write('\b') # efface le précédent caractère

convert = int(temp - 273.15)  # convertir les fahrenheit en celsius

#from googletrans import  Translator
#trad = Translator()
#descr = trad.translate(description, src='en', dest='fr')
print(weatherprint.format(weathercity, convert, description, gps))
