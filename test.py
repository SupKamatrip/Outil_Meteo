import requests
import time
import sys
#import googletrans

# input va nous permettre de saisir le contenu de weathercity
weathercity = input("Météo pour quelle  ville ? : ")

# on récupère ci-dessus les données de la requetes web
weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+weathercity+'&appid=9db93bdd1a0d2f47617d2c9158a903fa')
url = ('http://api.openweathermap.org/data/2.5/weather?q='+weathercity+'&appid=9db93bdd1a0d2f47617d2c9158a903fa')

# Simulation d'un temps de chargement
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor  # yield retourne le générateur cursor ( au lieu de stocker on récupère l'info à la volée )
                          # s'éxécute qu'une seule fois

# liste en java de weather ( notre requete est stockée dans une liste)
data = weather.json()

for key, value in data.items():
  print(key, value)


# retourne les coordonnées gps de la station météo
gps = data['coord']

pays = data['sys']['country']

humidite = data['main']['humidity']

pression = data['main']['pressure']

temp = data['main']['temp']

venttemp = data['wind']['deg']

ventsp = data['wind']['speed']

description = data['weather'][0]['description']

print(data)

weatherprint = "\nActuellement en {} a {}, il fait actuellement {}°C avec {}: \n\n-Le taux d'humidité est de {}% et la pression " \
               "atmosphérique est de {} hPa.\n-Le vent souffle à {} m/s et sa température est de {}°C\n\nLes coordonnées GPS de la station météo " \
               "sont {}."

# on fait appel à notre fonction précédemment définie
spinner = spinning_cursor()

# le _ permet d'ignorer l'itération, peut importe là ou ca en est la boucle est lancée
for _ in range(25):

    # nous permet d'écrire/afficher le logo de chargement
    sys.stdout.write(next(spinner))

    # Affiche immediatement le curseur plutot que d'attendre que le tampon soit plein
    sys.stdout.flush()

    # mets en pause 0.1 seconde a chaque itération dans la boucle for
    time.sleep(0.1)

    # efface le précédent caractère
    sys.stdout.write('\b')

# convertir les kelvin en celsius
convert = int(temp - 273.15)
convert2 = int(venttemp - 273.15)


#convert2 = int(tempressentie - 273.15)
#from googletrans import  Translator
#trad = Translator()
#descr = trad.translate(description, src='en', dest='fr')
print(weatherprint.format(pays, weathercity, convert, description, humidite, pression, ventsp, convert2, gps))
