import requests

def get_binance_data(symbol):
    url = f'https://api.binance.com/api/v3/ticker/bookTicker?symbol={symbol}'
    response = requests.get(url)
    data = response.json()
    return data

def fetch_prices(currency_pairs):
    prices = {}
    for pair in currency_pairs:
        data = get_binance_data(pair)
        prices[pair] = {'bid': data['bidPrice'], 'ask': data['askPrice']}
    return prices

def fetch_historical_data(symbol, interval='1h', limit=500):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)
    data = response.json()
    return data
