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


def get_weather(id_ville) :
    param = {
       "units" : "metric",
       "lang" : "fr"
    }
    url = f"{root_url}&id={id_ville}&appid={api_key}&units=metric&lang=fr"
    
    # url = f"{root_url}&lat={latitude}&lon={longitude}&appid={api_key}"
    r = requests.get(url, param)
    if r.status_code == 200 :
       for key in r :
          print(key)
    

def trouver_ville(ville_rechercher) :
  
  ville_trouver = [item for item in data if item["name"] == ville_rechercher]
  index = 1
  for ville in ville_trouver :
    
     print(f'{index} : {ville["name"]} |  {ville["country"]}')
     index += 1
  choice = input("Entrez le numéro de la ville désiré : ")
  choice = int(choice)
  ville_selectionner = ville_trouver[choice-1]
  return (ville_selectionner["id"])

def user_input():
    ville = input('Rechercher une ville. ')
    try:
      ville_found = trouver_ville(ville)
    except :
      print("An error is occured")
      exit()
    else:
       return ville_found

def main():
    get_weather(user_input())

main()