# My Flask Blog 📝

Welcome to the "My Flask Blog" repository! This updated project offers a dynamic and multifaceted blogging platform powered by Flask. The blog not only showcases creative writing but also integrates extra features such as gender and age guessing, live weather updates, and a robust finance section that provides stock data. Dive into this documentation to get started with setting up, navigating the new features, and contributing to the project.

![image](https://github.com/omerhalid/blog_flask/assets/102431713/d11bd582-cdf9-425e-a4da-f4131e2c1aa9)

![image](https://github.com/omerhalid/blog_flask/assets/102431713/6c377b4f-7f9d-47fe-adea-63f9250171b1)

![image](https://github.com/omerhalid/blog_flask/assets/102431713/7b42ee05-3143-4155-83e0-6ad5c3303a8e)

![image](https://github.com/omerhalid/blog_flask/assets/102431713/d203c661-3499-4563-862b-3e474cd86d9c)

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
