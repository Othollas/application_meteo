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

API_KEY = os.getenv("API_KEY")

for name in data :
    if name["name"] == "Villeneuve" :
        print(name)

def get_weather(ville) :
    api_keys = API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/"

    # Effectuer la requete API 
    params = {
        "q": ville,
        "appid": api_keys,
        "units": "metric", #Pour afficher les températures en celsius
        "lang": "fr" # Pour des descriptions en français
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200: 
        data = response.json()

        weather_info = {
            "ville":data["name"],
            "température":data["main"]["temp"],
            "description":data["weather"][0]["description"]
        }
        return weather_info
    else:
        print("erreur : Impossible de récupérer les données météo.")
        return None

