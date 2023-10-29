from flask import Flask, render_template 
import random
import time
import requests

app = Flask(__name__)

@app.route('/')
def index():
        current_year = time.localtime()[0]
        current_month = time.localtime()[1]
        current_day = time.localtime()[2]
        random_number = random.randint(1, 10)
        return render_template('index.html', num = random_number, year = current_year, month = current_month, day = current_day)

@app.route('/guess/<name>')
def guess(name):
        gender_url = f"https://api.genderize.io?name={name}"
        gender_response = requests.get(gender_url)
        gender_data = gender_response.json()
        gender = gender_data["gender"]
        
        age_url = f"https://api.agify.io?name={name}"
        age_response = requests.get(age_url)
        age_data = age_response.json()
        age = age_data["age"]
        return render_template('guess.html', name = name, gender = gender, age = age)

@app.route('weather/<city>')
def weather(city):
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3a6e6b1c9d0b8d2e3f7f7f8d6a4b9e3a"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        weather = weather_data["weather"]
        return render_template('weather.html', weather = weather)

if __name__ == '__main__':
        app.run(debug=True)
        