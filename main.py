# import du module requests pour faire de requette à la base de donnée
import requests
# Import de os pour recuperer la global d'environnement
import os
# import de load_dotenv afin de recuperer le fichier .env et le lire dans le script
from dotenv import load_dotenv
# Import de module json
import json
# Import du module datetime
from datetime import datetime

# Import du .env
load_dotenv()

#Ouverture du fichier Json contenant les informations relatives aux villes
with open("city.list.json", "r", encoding="utf-8") as f :
    data = json.load(f)

api_key = os.getenv("API_KEY")
root_url = "http://api.openweathermap.org/data/2.5/weather?"



def get_weather(id_ville) :

    url = f"{root_url}&id={id_ville}&appid={api_key}&units=metric&lang=fr"
    response = requests.get(url)

    if response.status_code != 200 :
        return {"error": "Ville introuvable ou problème avec l'API."}
    response = response.json()
  
    # Transformation du timeStamp en H/M/S 
    data_time = {"sunrise" : response["sys"]['sunrise'], "sunset" : response["sys"]['sunset']}
    timezone_offset = response["timezone"]
    sunrise_time = datetime.fromtimestamp(data_time["sunrise"] + timezone_offset -3600)
    sunset_time = datetime.fromtimestamp(data_time["sunset"] + timezone_offset - 3600)

    # modele pour les données
    return {
        "ville" :                       f"Ville : {response["name"]}",
        "current_weather" : f"Le ciel est {response["weather"][0]["description"]}",
        "temp" :            f"La température est de {response["main"]["temp"]}° | Ressentie : {response["main"]["feels_like"]}° | Min : {response["main"]["temp_min"]}° | Max : {response["main"]["temp_max"]}°",
        "sunrise_sunset" :  f"Lever de soleil : {sunrise_time.strftime("%H:%M:%S")} | Coucher de soleil : {sunset_time.strftime("%H:%M:%S")}"
    }


def trouver_ville(ville_rechercher) :
  ville_trouver = [item for item in data if item["name"].lower() == ville_rechercher.lower()]
  
  if not ville_trouver:
    return None
  return ville_trouver[0]["id"]


def get_weather_data(ville):
  ville_id = trouver_ville(ville)
  if ville_id:
      return get_weather(ville_id)
  return {"error": f"Ville non trouvée dans la base de données"}


#lancer le programme seul ou de l'importer dans Flask
if __name__ == "__main__":
  ville = input("Rechercher une ville : ")
  meteo = get_weather_data(ville)
  print(meteo)