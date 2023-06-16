from binance_api import fetch_prices, fetch_historical_data, generate_ws_url
from data_processing import convert_to_log, parse_historical_data
from arbitrage_analysis import calculate_log_rates, check_arbitrage_opportunities, calculate_historical_log_rates, estimate_no_arbitrage_bounds, plot_data
import logging
import websocket
import json

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

prices = {}

def on_message(ws, message, currency_pairs, no_arbitrage_bounds):
    data = json.loads(message)
    stream = data['stream']
    symbol = stream.split('@')[0].upper()
    bid_price = float(data['data']['b'])
    ask_price = float(data['data']['a'])
    prices[symbol] = {'bid': bid_price, 'ask': ask_price}
    print(f"Updated prices: {prices}")

    # Perform triangular arbitrage analysis with the updated prices
    log_prices = convert_to_log(prices)
    current_log_rates = calculate_log_rates(log_prices, currency_pairs)
    arbitrage_opportunities = check_arbitrage_opportunities(current_log_rates, no_arbitrage_bounds)
    print(f"Arbitrage opportunities: {arbitrage_opportunities}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws):
    print("WebSocket closed")

def on_open(ws):
    print("WebSocket opened")

def start_real_time_analysis(currency_pairs, no_arbitrage_bounds):
    ws_url = generate_ws_url(currency_pairs)

    ws = websocket.WebSocketApp(
        ws_url,
        on_message=lambda ws, message: on_message(ws, message, currency_pairs, no_arbitrage_bounds),
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()

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
    

    # Plot the no-arbitrage bounds
    plot_data(no_arbitrage_bounds['loop1'], "No-Arbitrage Bounds - Loop 1", "static/no_arbitrage_bounds_loop1.png")
    plot_data(no_arbitrage_bounds['loop2'], "No-Arbitrage Bounds - Loop 2", "static/no_arbitrage_bounds_loop2.png")


    # Calculate current log rates
    current_log_rates = calculate_log_rates(log_prices, currency_pairs)

    # Check for arbitrage opportunities
    arbitrage_opportunities = check_arbitrage_opportunities(current_log_rates, no_arbitrage_bounds)

    return {
        'no_arbitrage_bounds': no_arbitrage_bounds,
        'arbitrage_opportunities': arbitrage_opportunities
    }