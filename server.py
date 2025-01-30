from flask import Flask, render_template, request
from main import get_weather_data 

app = Flask(__name__)

@app.route('/', methods={"GET", "POST"})
def index():
    meteo = None

    if request.method == "POST":
        ville = request.form["ville"]
        meteo = get_weather_data(ville)

    return render_template('index.html', meteo=meteo)

if __name__ == "__main__":
    app.run(debug=True)