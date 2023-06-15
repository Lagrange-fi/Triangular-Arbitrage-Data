import numpy as np
import datetime

def convert_to_log(prices):
    return {pair: {'bid_log': np.log(float(price_data['bid'])), 'ask_log': np.log(float(price_data['ask']))} for pair, price_data in prices.items()}

def parse_historical_data(data):
    parsed_data = []
    for entry in data:
        timestamp = datetime.datetime.fromtimestamp(entry[0] / 1000)
        open_price = float(entry[1])
        high_price = float(entry[2])
        low_price = float(entry[3])
        close_price = float(entry[4])
        parsed_data.append({
            'timestamp': timestamp,
            'open': open_price,
            'high': high_price,
            'low': low_price,
            'close': close_price
        })
    return parsed_data