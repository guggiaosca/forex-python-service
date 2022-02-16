from forex_python.converter import CurrencyRates
from flask import Flask, request, jsonify

app = Flask(__name__)
c = CurrencyRates()

@app.get("/rates")
def get_rates():
    return c.get_rates('USD')



#currencies = ["USD", "GBP", "EUR", "BRL"]
#for currency in currencies:
#print(currency + "->USD: " + str(c.get_rate(currency, "USD")) )