import numpy as np
import datetime
import logging

def convert_to_log(prices):
    logging.info("Converting prices to logarithmic form")
    log_prices = {
        pair: {
            'bid_log': np.log(float(price_data['bid'])),
            'ask_log': np.log(float(price_data['ask']))
        } for pair, price_data in prices.items()
    }
    logging.info("Prices converted to logarithmic form")
    return log_prices

def parse_historical_data(data):
    logging.info("Parsing historical data")
    parsed_data = [{
        'date': datetime.datetime.fromtimestamp(entry[0] / 1000),
        'timestamp': datetime.datetime.fromtimestamp(entry[0] / 1000),
        'open': float(entry[1]),
        'high': float(entry[2]),
        'low': float(entry[3]),
        'close': float(entry[4])
    } for entry in data]
    logging.info("Historical data parsed")
    return parsed_data