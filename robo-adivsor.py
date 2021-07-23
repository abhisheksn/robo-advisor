#roboadvisor.py
import os
import requests
from dotenv import load_dotenv  # source:https://github.com/theskumar/python-dotenv
import json
from datetime import datetime

load_dotenv()

#Converting numeric value to USD formatted string
#source: Professor Rossetti
def to_usd(my_price):
    return f"${my_price:,.2f}"


#Obtaining the date and time for printing receipt
#source:https://www.programiz.com/python-programming/datetime/current-datetime
now = datetime.today()
dt_string = now.strftime("%Y/%m/%d %I:%M %p")

#USER_INPUT
symbol = input("Please input the Stock symbol:")

#Alter the tax rate by creating a .env file
# source:https://github.com/theskumar/python-dotenv
API = os.getenv("API_KEY")

STOCK_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}"

stock_request = requests.get(STOCK_URL)
stocks_data = json.loads(stock_request.text)
last_refresh = stocks_data["Meta Data"]["3. Last Refreshed"]

tsd = stocks_data["Time Series (Daily)"]

dates = list(tsd.keys())
latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high=max(high_prices)
recent_low=min(high_prices)

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {dt_string}")
print("-------------------------")
print(f"LATEST DAY: {latest_day}")
print(f"LATEST CLOSE: {latest_close}")
print(f"RECENT HIGH: {recent_high}")
print(f"RECENT LOW: {recent_low}")
print("-------------------------")
#print("RECOMMENDATION: BUY!")
#print("RECOMMENDATION REASON:")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
