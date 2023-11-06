from flask import Flask, jsonify, redirect, render_template, request, url_for
import random
import time
import requests
import os
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from schemas import City, Stock, db, BuyStock, User, Contact, ContactWhoSendEmail
import bcrypt
import smtplib

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db.init_app(app)
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

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data['username']
    password = data['password'].encode('utf-8')  # encode the password to bytes

    # Check if user already exists
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({"error": "Username already taken"}), 400

    # Hash the password
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    # Create a new user with the hashed password
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/contact', methods=['POST'])
def contact():
        if request.method == 'POST':
                data = request.get_json()
                if not data:
                        return jsonify({"error: no data"}), 400
                
                name = data['name']
                email = data['email']
                message =data['message']
                
                contact = Contact(name=name, email=email, message=message)
                
                db.session.add(contact)
                db.session.commit()
                
                return jsonify({"message": message}), 201

#send emal from contact form using smtp
@app.route('/contact/send', methods=['POST'])
def send_email():
        data = request.get_json()
        if not data:
                return jsonify({"error: no data"}), 400
        name = data['name']
        email = data['email']
        message =data['message']
        email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage: {message}"
        email_message = email_message.encode('utf-8')
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))
                connection.sendmail(from_addr=os.getenv("EMAIL"), to_addrs=os.getenv("EMAIL"), msg=email_message)
        is_sent_email = True
        contactWhoSendEmail = ContactWhoSendEmail(name=name, email=email, message=message, is_sent_email=is_sent_email)
        db.session.add(contactWhoSendEmail)
        db.session.commit()
        return jsonify({"message": "Email sent successfully!", "content": message}), 201

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
        
        stock_name = request.args.get('stock')  
        stock = Stock(stock=stock_name)
        db.session.add(stock)
        db.session.commit()
        
        stock = request.args.get('stock')
        if stock:
                #Redirect to the stock details page
                return redirect(url_for('get_stock_data', stock=stock.upper())) 
        else:
                #Handle the case where no stock symbol is provided
                return render_template('finance.html', error="Please provide a stock symbol")
        
#stock buy and sell endpoint
@app.route("/finance/buy/<stock>", methods=["POST"])
def buy_stock(stock):
        
        api_key = os.getenv("ALPHAVANTAGE_API_KEY")
        ts = TimeSeries(key=api_key, output_format='json')
        data, _ = ts.get_quote_endpoint(symbol=stock)
        stock_data = {
                "symbol": stock.upper(),
                "price": data.get('05. price', "N/A"),
                "open": data.get('02. open', "N/A"),
                "high": data.get('03. high', "N/A"),
                "low": data.get('04. low', "N/A"),
                "volume": data.get('06. volume', "N/A"),
                }
        
        data = request.get_json()
        if not data:
                return jsonify({"error": "Invalid data"}), 400
        
        #stock_name = data.get("stock") #we don't need this because we already have the stock name in the url
        #stock_price = data.get("price")
        stock_price = float(stock_data.get("price"))
        stock_quantity = data.get("quantity")
        
        total_value = stock_price * stock_quantity
        
        stock = BuyStock(stock=stock, price=stock_price, quantity=stock_quantity, total=total_value)
        db.session.add(stock)
        db.session.commit()
        
        return jsonify({"message": "Stock bought successfully!"}), 200
        #TO DO: fix the redirect to the buy_stock.html page
        #return render_template('buy_stock.html', stock=stock)

#get request to see all the stocks bought
@app.route("/finance/buy", methods=["GET"])
def get_all_stocks():
        
        stocks = BuyStock.query.all()
        all_stocks = []
        for stock in stocks:
                stock_data = {
                        "stock": stock.stock,
                        "price": stock.price,
                        "quantity": stock.quantity,
                        "total": stock.total
                }
                all_stocks.append(stock_data)
        return jsonify({"stocks": all_stocks}), 200
        
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
