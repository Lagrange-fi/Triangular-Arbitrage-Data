from binance_api import fetch_prices, fetch_historical_data
from data_processing import convert_to_log, parse_historical_data
from arbitrage_analysis import calculate_log_rates, check_arbitrage_opportunities, calculate_historical_log_rates, estimate_no_arbitrage_bounds
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def run_analysis(currency_pairs):
    # Fetch prices
    prices = await fetch_prices(currency_pairs)

    # Convert prices to logarithmic form
    log_prices = convert_to_log(prices)

    # Fetch historical data
    historical_data = {}
    for pair in currency_pairs:
        data = fetch_historical_data(pair)
        historical_data[pair] = data

    # Parse historical data
    parsed_historical_data = {}
    for pair, data in historical_data.items():
        parsed_data = parse_historical_data(data)
        parsed_historical_data[pair] = parsed_data

    historical_log_rates = calculate_historical_log_rates(parsed_historical_data, currency_pairs)

    # Estimate no-arbitrage bounds
    no_arbitrage_bounds = estimate_no_arbitrage_bounds(historical_log_rates)

    # Calculate current log rates
    current_log_rates = calculate_log_rates(log_prices, currency_pairs)

    # Check for arbitrage opportunities
    arbitrage_opportunities = check_arbitrage_opportunities(current_log_rates, no_arbitrage_bounds)

    return {
        'no_arbitrage_bounds': no_arbitrage_bounds,
        'arbitrage_opportunities': arbitrage_opportunities
    }