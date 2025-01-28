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
latitude = None
longitude = None


def get_weather(id_ville) :
    # param = {
    #    "units" : "metric",
    #    "lang" : "fr"
    # }
    # url = f"{root_url}&lat={latitude}&lon={longitude}&appid={api_key}"
    url = f"{root_url}&id={id_ville}&appid={api_key}&units=metric&lang=fr"
    
    
    r = requests.get(url, param)
    if r.status_code == 200 :
        response = r.json()
        for key in response:
           print(key)

    # Transformation du timeStamp en H/M/S 
    data_time = {"sunrise" : response["sys"]['sunrise'], "sunset" : response["sys"]['sunset']} 
    sunrise_time = datetime.fromtimestamp(data_time["sunrise"])
    sunset_time = datetime.fromtimestamp(data_time["sunset"])

    # modele pour les données
    modele = {
        "ville" :                       f"Ville : {response["name"]}",
        "current_weather" : f"Le ciel est {response["weather"][0]["description"]}",
        "temp" :            f"La température est de {response["main"]["temp"]}° | Ressentie : {response["main"]["feels_like"]}° | Min : {response["main"]["temp_min"]}° | Max : {response["main"]["temp_max"]}°",
        "sunrise_sunset" :  f"Lever de soleil : {sunrise_time.strftime("%H:%M:%S")} | Coucher de soleil : {sunset_time.strftime("%H:%M:%S")}"
    }

    # Affichage du resultat
    print(f"""
        {modele["ville"]}
        {modele['current_weather']}
        {modele["temp"]}
        {modele["sunrise_sunset"]}
""")    

#     print(f"""
#     Ville :         {response["name"]}
#     Température :   {response["weather"]}
#     timezone :      {response["timezone"]}
#     base :          {response["base"]}
#     main :          {response["main"]}
#     visibility :    {response["visibility"]}
#     wind :          {response["wind"]}
#     dt :            {response["dt"]}
#     sys :           {response["sys"]}

# """)

# Choisir une ville quand les resultats sont multiples.
def trouver_ville(ville_rechercher) :
  ville_trouver = [item for item in data if item["name"].lower() == ville_rechercher.lower()]
  index = 1
  if len(ville_trouver) > 1:
    for ville in ville_trouver :
        print(f'{index} : {ville["name"]} |  {ville["country"]}')
        index += 1
    choice = input("Entrez le numéro de la ville désiré : ")
    choice = int(choice)
    ville_selectionner = ville_trouver[choice-1]
    return (ville_selectionner["id"])
  else:
    return ville_trouver[0]["id"]
  
# Utilisation du try except pour gerer les errreurs
def user_input():
    ville = input('Rechercher une ville. ')
    try:
      ville_found = trouver_ville(ville)
    except:
      print("An error is occured ")
      exit()
    else:
       return ville_found

# Fonction qui combine les fonction de l'application
def main():
    get_weather(user_input())


#lancer le programme
main()