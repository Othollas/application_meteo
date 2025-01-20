# import du module requests pour faire de requette à la base de donnée
import requests
# Import de os pour recuperer la global d'environnement
import os
# import de load_dotenv afin de recuperer le fichier .env et le lire dans le script
from dotenv import load_dotenv
import json


load_dotenv()

with open("city.list.json", "r", encoding="utf-8") as f :
    data = json.load(f)

api_key = os.getenv("API_KEY")
root_url = "http://api.openweathermap.org/data/2.5/weather?"
latitude = None
longitude = None

# def get_lat_and_lon(ville_rechercher) :
#   ville_trouver = {ville for ville in data["name"] if ville == ville_rechercher}
#   return ville_trouver

def get_weather(ville) :
    url = f"{root_url}&lat={latitude}&lon={longitude}&appid={api_key}"
    r = requests.get(url)
    


    # # Effectuer la requete API 
    # params = {
    #     "q": ville,
    #     "appid": api_keys,
    #     "units": "metric", #Pour afficher les températures en celsius
    #     "lang": "fr" # Pour des descriptions en français
    # }
    # response = requests.get(base_url, params=params)

    # if response.status_code == 200: 
    #     data = response.json()

    #     weather_info = {
    #         "ville":data["name"],
    #         "température":data["main"]["temp"],
    #         "description":data["weather"][0]["description"]
    #     }
    #     return weather_info
    # else:
    #     print("erreur : Impossible de récupérer les données météo.")
    #     return None

# town = input("quel ville ? ")
# print(get_lat_and_lon(town))
def trouver_ville(ville_rechercher) :
  ville_trouver = [item for item in data if item["name"] == ville_rechercher]
  index = 1
  for ville in ville_trouver :
    
     print(f'{index} : {ville["name"]} |  {ville["country"]}')
     index += 1
  choice = input("Entrez le numéro de la ville désiré : ")
  choice = int(choice)
  ville_selectionner = ville_trouver[choice-1]
  return (ville_selectionner["coord"])
      # faire une boucle dans ville_trouver pour recueprer le nom de la ville et le pays de la ville 



# Configurer la variable d'environnement

# Configurer les divers modules nécessaires

# Importer et lire le fichier json contenant les Latitudes et Longitudes des villes recherchées 

# Definir une fonction qui prendra en parametre le nom de la ville à chercher 
# Possibilité de plusieurs villes trouvé dans differents pays, donc nous devons le trier, pour ça il faut :
#  1\ afficher les noms des villes et leur pays attribués dans une liste et laisser l'utilisateur choisir 
#  2\ Une fois le choix effectué le mettre dans une variable et retrourner la variable


# Definir une fonction qui recuperera tout les parametre deja crée et qui iras chercher la bonne ville pour recuperer les donnée 
# Les données seront triées pour etre afficher. avec la température, le taux d'humidité, la precipitation etc...

print(trouver_ville("Bordeaux"))