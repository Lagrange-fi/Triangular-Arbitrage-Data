import requests
import logging

session = requests.Session()

def get_binance_data(symbol):
    logging.info(f"Fetching data for {symbol}")
    try:
        url = f'https://api.binance.com/api/v3/ticker/bookTicker?symbol={symbol}'
        response = session.get(url)
        data = response.json()
        logging.info(f"Data fetched for {symbol}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None
    
def fetch_prices(currency_pairs):
    prices = {}
    for pair in currency_pairs:
        data = get_binance_data(pair)
        prices[pair] = {'bid': data['bidPrice'], 'ask': data['askPrice']}
    return prices

def fetch_available_pairs():
    url = "https://api.binance.com/api/v3/exchangeInfo"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error fetching available pairs:", e)
        return []

    data = response.json()

    if 'symbols' not in data:
        print("Error fetching available pairs:", data)
        return []

    available_pairs = [symbol['symbol'] for symbol in data['symbols'] if symbol['status'] == 'TRADING']
    return available_pairs

def fetch_historical_data(symbol, interval='1h', limit=500):
    logging.info(f"Fetching historical data for {symbol}")
    try:
        url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
        response = session.get(url)
        data = response.json()
        logging.info(f"Historical data fetched for {symbol}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None