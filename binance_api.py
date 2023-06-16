import requests
import logging

def get_binance_data(symbol):
    logging.info(f"Fetching data for {symbol}")
    try:
        url = f'https://api.binance.com/api/v3/ticker/bookTicker?symbol={symbol}'
        response = requests.get(url)
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

def fetch_historical_data(symbol, interval='1h', limit=500):
    logging.info(f"Fetching historical data for {symbol}")
    try:
        url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
        response = requests.get(url)
        data = response.json()
        logging.info(f"Historical data fetched for {symbol}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None
