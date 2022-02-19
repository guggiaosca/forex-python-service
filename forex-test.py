from forex_python.converter import CurrencyRates

c = CurrencyRates()
currencies = ["USD", "GBP", "EUR", "BRL"]
for currency in currencies:
    print(currency + "->USD: " + str(c.get_rate(currency, "USD")) )