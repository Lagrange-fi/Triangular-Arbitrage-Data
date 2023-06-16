import numpy as np
import logging
import concurrent.futures

def _calculate_log_rate_single_loop(args):
    log_prices, currency_pairs, loop = args
    if loop == 'loop1':
        return log_prices[currency_pairs[0]]['ask_log'] + log_prices[currency_pairs[2]]['bid_log'] - log_prices[currency_pairs[1]]['bid_log']
    elif loop == 'loop2':
        return log_prices[currency_pairs[3]]['ask_log'] + log_prices[currency_pairs[4]]['ask_log'] - log_prices[currency_pairs[5]]['bid_log']

def calculate_log_rates(log_prices, currency_pairs):
    logging.info("Calculating log rates")
    logging.debug(f"log_prices: {log_prices}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        args = [(log_prices, currency_pairs, loop) for loop in ['loop1', 'loop2']]
        log_rates = list(executor.map(_calculate_log_rate_single_loop, args))

    log_rates_dict = {'loop1': log_rates[0], 'loop2': log_rates[1]}
    logging.info("Log rates calculated")
    return log_rates_dict

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

def calculate_historical_log_rates(parsed_historical_data, currency_pairs):
    logging.info("Calculating historical log rates")
    historical_log_rates = {'loop1': [], 'loop2': []}
    pair1_close = np.array([entry['close'] for entry in parsed_historical_data[currency_pairs[0]]])
    pair2_close = np.array([entry['close'] for entry in parsed_historical_data[currency_pairs[1]]])
    pair3_close = np.array([entry['close'] for entry in parsed_historical_data[currency_pairs[2]]])
    pair4_close = np.array([entry['close'] for entry in parsed_historical_data[currency_pairs[3]]])
    pair5_close = np.array([entry['close'] for entry in parsed_historical_data[currency_pairs[4]]])
    pair6_close = np.array([entry['close'] for entry in parsed_historical_data[currency_pairs[5]]])

    
    loop1 = np.log(pair1_close) + np.log(pair3_close) - np.log(pair2_close)
    loop2 = np.log(pair4_close) + np.log(pair5_close) - np.log(pair6_close)
    
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