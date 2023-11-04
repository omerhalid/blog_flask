from flask import Flask, jsonify, redirect, render_template, request, url_for
import random
import time
import requests
import os
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.city import db, City

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create the tables in the database
#db.create_all()

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

stocks = {
        '1': 'Apple Inc. - AAPL',
        '2': 'Microsoft Corporation - MSFT',
        '3': 'Amazon.com, Inc. - AMZN',
        '4': 'Facebook, Inc. - FB',
        '5': 'Alphabet Inc. (Google) - GOOGL',
        '6': 'Tesla, Inc. - TSLA',
        '7': 'NVIDIA Corporation - NVDA',
        '8': 'PayPal Holdings, Inc. - PYPL',
        '9': 'Netflix, Inc. - NFLX',
        '10': 'Adobe Inc. - ADBE',
        '11': 'Intel Corporation - INTC',
        '12': 'Cisco Systems, Inc. - CSCO',
        '13': 'Comcast Corporation - CMCSA',
        '14': 'PepsiCo, Inc. - PEP',
        '15': 'Adobe Inc. - ADBE',
        '16': 'Broadcom Inc. - AVGO',
        '17': 'Texas Instruments Incorporated - TXN',
        '18': 'QUALCOMM Incorporated - QCOM',
        '19': 'Costco Wholesale Corporation - COST',
        '20': 'Starbucks Corporation - SBUX',
        '21': 'Amgen Inc. - AMGN',
        '22': 'Charter Communications, Inc. - CHTR',
        '23': 'Gilead Sciences, Inc. - GILD',
        '24': 'Mondelez International, Inc. - MDLZ',
        '25': 'Automatic Data Processing, Inc. - ADP'
    }

def get_company_name_by_symbol(symbol, stocks):
    for key, value in stocks.items():
        company_name, company_symbol = value.split(' - ')
        if company_symbol.lower() == symbol.lower():
            return company_name
    return "Unknown Company"

@app.route("/finance")
def get_stock():
        return render_template('finance.html', stocks = stocks)

@app.route("/finance/<stock>", endpoint="get_stock_data")
def get_stock_data(stock):
        api_key = os.getenv("ALPHAVANTAGE_API_KEY")
        ts = TimeSeries(key=api_key, output_format='json')
        try:    
                data, _ = ts.get_quote_endpoint(symbol=stock)
                company_name = get_company_name_by_symbol(stock, stocks)
                stock_data = {
                "symbol": stock.upper(),
                "price": data.get('05. price', "N/A"),
                "open": data.get('02. open', "N/A"),
                "high": data.get('03. high', "N/A"),
                "low": data.get('04. low', "N/A"),
                "volume": data.get('06. volume', "N/A"),
                "company_name": company_name
                }
                return render_template('stock_details.html', stock_data=stock_data)
        except Exception as e:
                return jsonify({"error": str(e)}), 500   
        
#search the stock
@app.route("/finance/search", methods=["GET"])
def search_stock():
        stock = request.args.get('stock')
        if stock:
                #Redirect to the stock details page
                return redirect(url_for('get_stock_data', stock=stock.upper())) 
        else:
                #Handle the case where no stock symbol is provided
                return render_template('finance.html', error="Please provide a stock symbol")

#TO DO: activate the api key
@app.route('/weather', methods=['GET'])
def weather():
        
        city_name = request.args.get('city')  # replace with actual city name
        city = City(name=city_name)
        db.session.add(city)
        db.session.commit()
        
        API_KEY = os.getenv("API_KEY")
        
        city = request.args.get('city')  # Get the city from the form input name
        if not city:
                return "Please provide a city name.", 400
        
        try:
                weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
                weather_response = requests.get(weather_url)
                weather_data = weather_response.json()

                # Convert Kelvin to Celsius
                temperature_kelvin = weather_data["main"]["temp"]
                temperature_celsius = temperature_kelvin - 273.15

                # Parsing some data to be displayed in the weather template
                weather = {
                        "description": weather_data["weather"][0]["description"],
                        "temperature": round(temperature_celsius, 2),  # Rounded to 2 decimal places
                        "city": weather_data["name"]
                }
                
                return render_template('weather.html', weather=weather)
        except Exception as e:
                return str(e), 500
        

if __name__ == "__main__":
    app.run(debug=True)
