from forex_python.converter import CurrencyRates
from flask import Flask, request, jsonify

app = Flask(__name__)
c = CurrencyRates()

@app.get("/rates")
def get_rates():
    return c.get_rates('USD')

@app.get("/rates/<code>")
def get_ratesById(code):
    return c.get_rates(code)
