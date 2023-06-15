import numpy as np

def calculate_log_rates(log_prices):
    loop1 = log_prices['BTCUSDT']['ask_log'] + log_prices['BTCEUR']['bid_log'] - log_prices['EURUSDT']['bid_log']
    loop2 = log_prices['USDTTRY']['ask_log'] + log_prices['BTCTRY']['ask_log'] - log_prices['BTCUSDT']['bid_log']
    return {'loop1': loop1, 'loop2': loop2}

def check_arbitrage_opportunities(log_rates, no_arbitrage_bounds):
    opportunities = {}
    for loop, rate in log_rates.items():
        if rate > no_arbitrage_bounds[loop]['upper'] or rate < no_arbitrage_bounds[loop]['lower']:
            opportunities[loop] = True
        else:
            opportunities[loop] = False
    return opportunities

def calculate_historical_log_rates(parsed_historical_data):
    historical_log_rates = {'loop1': [], 'loop2': []}
    for data in zip(parsed_historical_data['BTCUSDT'], parsed_historical_data['EURUSDT'], parsed_historical_data['BTCEUR'], parsed_historical_data['USDTTRY'], parsed_historical_data['BTCTRY']):
        btcusdt, eurusdt, btceur, usdttry, btctry = data
        loop1 = np.log(btcusdt['close']) + np.log(btceur['close']) - np.log(eurusdt['close'])
        loop2 = np.log(usdttry['close']) + np.log(btctry['close']) - np.log(btcusdt['close'])
        historical_log_rates['loop1'].append(loop1)
        historical_log_rates['loop2'].append(loop2)
    return historical_log_rates

def estimate_no_arbitrage_bounds(historical_log_rates, confidence_interval=0.95):
    no_arbitrage_bounds = {}
    for loop, rates in historical_log_rates.items():
        mean = np.mean(rates)
        std_dev = np.std(rates)
        z_score = abs(np.percentile(rates, (1 - confidence_interval) / 2))
        no_arbitrage_bounds[loop] = {
            'upper': mean + z_score * std_dev,
            'lower': mean - z_score * std_dev
        }
    return no_arbitrage_bounds