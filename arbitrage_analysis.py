import numpy as np
import logging

def calculate_log_rates(log_prices):
    logging.info("Calculating log rates")
    loop1 = log_prices['BTCUSDT']['ask_log'] + log_prices['BTCEUR']['bid_log'] - log_prices['EURUSDT']['bid_log']
    loop2 = log_prices['USDTTRY']['ask_log'] + log_prices['BTCTRY']['ask_log'] - log_prices['BTCUSDT']['bid_log']
    log_rates = {'loop1': loop1, 'loop2': loop2}
    logging.info("Log rates calculated")
    return log_rates

def check_arbitrage_opportunities(log_rates, no_arbitrage_bounds):
    logging.info("Checking arbitrage opportunities")
    opportunities = {}
    for loop, rate in log_rates.items():
        if rate > no_arbitrage_bounds[loop]['upper'] or rate < no_arbitrage_bounds[loop]['lower']:
            opportunities[loop] = True
        else:
            opportunities[loop] = False
    logging.info("Arbitrage opportunities checked")
    return opportunities

def calculate_historical_log_rates(parsed_historical_data):
    logging.info("Calculating historical log rates")
    historical_log_rates = {'loop1': [], 'loop2': []}
    btcusdt_close = np.array([entry['close'] for entry in parsed_historical_data['BTCUSDT']])
    eurusdt_close = np.array([entry['close'] for entry in parsed_historical_data['EURUSDT']])
    btceur_close = np.array([entry['close'] for entry in parsed_historical_data['BTCEUR']])
    usdttry_close = np.array([entry['close'] for entry in parsed_historical_data['USDTTRY']])
    btctry_close = np.array([entry['close'] for entry in parsed_historical_data['BTCTRY']])
    
    loop1 = np.log(btcusdt_close) + np.log(btceur_close) - np.log(eurusdt_close)
    loop2 = np.log(usdttry_close) + np.log(btctry_close) - np.log(btcusdt_close)
    
    historical_log_rates['loop1'] = loop1.tolist()
    historical_log_rates['loop2'] = loop2.tolist()
    logging.info("Historical log rates calculated")
    return historical_log_rates

def estimate_no_arbitrage_bounds(historical_log_rates, confidence_interval=0.95):
    logging.info("Estimating no-arbitrage bounds")
    no_arbitrage_bounds = {}
    for loop, rates in historical_log_rates.items():
        mean = np.mean(rates)
        std_dev = np.std(rates)
        z_score = abs(np.percentile(rates, (1 - confidence_interval) / 2))
        no_arbitrage_bounds[loop] = {
            'upper': mean + z_score * std_dev,
            'lower': mean - z_score * std_dev
        }
    logging.info("No-arbitrage bounds estimated")
    return no_arbitrage_bounds