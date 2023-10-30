from flask import Flask, render_template 
import random
import time
import requests

app = Flask(__name__)

@app.route('/')
def homex():
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

@app.route("/blog")
def get_blog():
         #just to see what is being passed in
        #blog_url = "https://api.npoint.io/c790b4d5cab58020d391" from 100 days of code
        blog_url = "https://api.npoint.io/8946b91f17f797e529e4" # for sorting algorithms
        response = requests.get(blog_url)
        all_posts = response.json()
        return render_template('blog.html', posts = all_posts)


# @app.route('weather/<city>')
# def weather(city):
#         weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={}"
#         weather_response = requests.get(weather_url)
#         weather_data = weather_response.json()
#         weather = weather_data["weather"]
#         return render_template('weather.html', city = city, weather = weather)

if __name__ == "__main__":
    app.run(debug=True)
