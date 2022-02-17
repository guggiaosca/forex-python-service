from forex_python.converter import CurrencyRates
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
c = CurrencyRates()

@app.get("/rates")
def get_rates():
    return c.get_rates('USD')

@app.get("/rates/<code>")
def get_ratesById(code):
    args = request.args;
    exchange_date = args.get("exchange_date")
    convert_to = args.get("currency")
    if None not in (exchange_date, convert_to):
        date_time_obj = datetime.datetime.strptime(exchange_date, '%Y-%m-%d')
        return str(c.get_rate(code, convert_to, date_time_obj))
    elif exchange_date is not None:
        date_time_obj = datetime.datetime.strptime(exchange_date, '%Y-%m-%d')
        return str(c.get_rate(code, date_time_obj))
    elif convert_to is not None:
        retorno = str(c.get_rate(code, convert_to))
        return retorno
    return c.get_rates(code)
