# My Flask Blog 📝

Welcome to the "My Flask Blog" repository! This updated project offers a dynamic and multifaceted blogging platform powered by Flask. The blog not only showcases creative writing but also integrates extra features such as gender and age guessing, live weather updates, and a robust finance section that provides stock data. Dive into this documentation to get started with setting up, navigating the new features, and contributing to the project.

![image](https://github.com/omerhalid/blog_flask/assets/102431713/d11bd582-cdf9-425e-a4da-f4131e2c1aa9)

![image](https://github.com/omerhalid/blog_flask/assets/102431713/6c377b4f-7f9d-47fe-adea-63f9250171b1)

![image](https://github.com/omerhalid/blog_flask/assets/102431713/7b42ee05-3143-4155-83e0-6ad5c3303a8e)

![image](https://github.com/omerhalid/blog_flask/assets/102431713/d203c661-3499-4563-862b-3e474cd86d9c)

# Database Models

The application's data storage is managed by a set of models that define the schema for the database. We're using SQLAlchemy as our ORM to interact with the database in an efficient and Pythonic way. Here's a brief overview of the models:

## City Model

- **Description**: Represents a city with weather-related data requirements.
- **Fields**:
  - `id`: A unique identifier for each city entry.
  - `name`: The name of the city, which cannot be null.

## Stock Model

- **Description**: Contains information about different stocks available in the application.
- **Fields**:
  - `id`: Unique identifier for each stock entry.
  - `ticker`: The ticker symbol for the stock, a unique set of characters representing a particular stock.

## BuyStock Model

- **Description**: Records the details of stock purchase transactions.
- **Fields**:
  - `id`: Unique identifier for each transaction.
  - `stock`: The ticker symbol of the purchased stock.
  - `price`: The price at which the stock was bought.
  - `quantity`: The number of shares bought.
  - `total`: The total value of the transaction (calculated as `price` * `quantity`).

These models help to structure and store important data for the application, allowing for powerful querying and data manipulation capabilities through SQLAlchemy.

![image](https://github.com/omerhalid/blog_flask/assets/102431713/80460d97-6828-49f5-8065-86f0a2dc6d87)


## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Configuration](#api-configuration)
- [Finance Section Usage](#finance-section-usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Dynamic Routing**: Each blog post has a unique URL. Utilize name-based gender and age guessing.
- **Responsive Design**: Adaptive and mobile-responsive to ensure a seamless experience on all devices.
- **Custom Styling**: Fresh and modern aesthetics for a clean and engaging user interface.
- **Weather Updates**: Get live weather forecasts by inputting a city name.
- **Finance Section**: An addition of a finance section that offers real-time stock market data.
- **API Integration**: The application now includes third-party APIs for gender and age estimation, weather forecasts, and stock market data.

### User Registration

- Users can now register an account with our service.
- The registration process is secure and passwords are hashed for protection.
- Upon successful registration, users receive a confirmation message.

### User Login (Functionality to be implemented)

- (Note: Add details about login once implemented, this section is reserved for future updates.)

### Contact Us

- A contact form is now available for users to send messages directly to the administration team.
- The backend handles the contact form submissions and uses SMTP to send an email to the admin.

## Implementation Details

### Security

- Passwords are securely hashed using `bcrypt` before being stored in the database.

### SMTP Email Integration

- When a user submits a contact form, the information is sent via email using `smtplib`.
- Environment variables are used to securely store email credentials.

## How to Use

### Registering a New User

- Send a `POST` request to `/register` with a JSON payload containing `username` and `password`.
- Example: `{"username": "newuser", "password": "password123"}`

### Sending a Message Through Contact Form

- Send a `POST` request to `/contact` with a JSON payload containing `name`, `email`, and `message`.
- The server will process the request and dispatch an email to the admin's email address configured in the environment variables.

## Prerequisites

Before you get started, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/YourGithubUsername/my-flask-blog.git
    cd my-flask-blog
    ```

2. **Set Up a Virtual Environment (Optional but Recommended):**

    ```bash
    python -m venv venv
    ```

    Then, activate the virtual environment:

    - For Windows:
        ```bash
        venv\Scripts\activate
        ```

    - For macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

3. **Install the Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

    *Note: The `requirements.txt` file should list all necessary dependencies, including Flask and any libraries required for API integration.*

## Running the Application

To run the application after the setup:

```bash
python app.py

# API Configuration

Before you start using the application, it's crucial to configure your API keys for the following services:

- **Gender and age prediction service**: This service will require an API key to access demographic data based on names or other submitted details.
- **Weather data service**: To fetch real-time weather information, an API key for a weather data provider is needed.
- **Financial data service**: For accessing stock prices, historical financial data, and other market insights, an API key from a financial data service is necessary.

## Storing API Keys

For security reasons, follow these best practices for storing your API keys:

- **Environment Variables**: Store your API keys in environment variables. This can be done in a `.env` file in your project's root directory, which should be added to `.gitignore` to ensure it's not tracked by version control.
- **Configuration File**: Alternatively, you can store them in a configuration file specifically designed for API keys, ensuring this file is also not tracked by version control.

# Finance Section Usage

The finance section of the application allows users to explore financial data. Here's how to use it:

1. **Navigate to `/finance` Endpoint**: Open your web browser or API client and go to the `/finance` endpoint of the application.
2. **Search Functionality**: Use the search feature to look up stock data. You can typically do this by entering the ticker symbol of the company you're interested in.
3. **Explore Insights and Articles**: Within the finance section, you can find various insights into financial data, as well as articles and analysis on market trends and stock performance.

## Search by Ticker Symbol

To query stock data by ticker symbol:

- Enter the ticker symbol in the search bar.
- Submit the search to retrieve financial information and historical data regarding the specific stock.

## Accessing Financial Insights

- In the finance section, navigate through the available resources.
- Read articles, analysis, and get insights that can help with investment decisions or understanding the market.

Remember to always keep your API keys confidential and to use the financial data in compliance with the terms of service of the API provider.
