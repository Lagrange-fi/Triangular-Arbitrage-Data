# Cryptocurrency Arbitrage Analysis

This project aims to identify potential arbitrage opportunities in the cryptocurrency market by analyzing price data from the Binance exchange. The analysis focuses on five currency pairs: BTCUSDT, EURUSDT, BTCEUR, USDTTRY, and BTCTRY. The project consists of four Python files: `binance_api.py`, `data_processing.py`, `main.py`, and `arbitrage_analysis.py`.

## Getting Started

Before running the project, make sure to install the required dependencies. You can do this by running the following command in your terminal or command prompt:
`pip install -r requirements.txt`
This will install the necessary packages listed in the `requirements.txt` file.

## Customizing Currency Pairs

If you want to analyze different currency pairs, you can easily do so by editing the `currency_pairs` array in the `main.py` file. For example:

`currency_pairs = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']`

Replace the existing currency pairs with the ones you want to analyze, then run the main.py script to perform the arbitrage analysis on the new currency pairs.

## Key Components

1. **Data Collection**: The `binance_api.py` file contains functions to fetch the latest bid and ask prices and historical data for the selected currency pairs using the Binance API.

2. **Data Processing**: The `data_processing.py` file processes the fetched data by converting bid and ask prices to their logarithmic form and parsing the historical data to extract relevant information.

3. **Arbitrage Analysis**: The `arbitrage_analysis.py` file contains functions to calculate log rates, and historical log rates, estimate no-arbitrage bounds and check for arbitrage opportunities.

4. **Main Script**: The `main.py` file is the main script that combines the functions from the other files to perform the complete analysis. It fetches and processes the data, calculates historical log rates, estimates no-arbitrage bounds, and checks for arbitrage opportunities.

## Workflow

1. Fetch the latest bid and ask prices for the selected currency pairs.
2. Convert the bid and ask prices to their logarithmic form.
3. Fetch and parse historical data for the currency pairs.
4. Calculate historical log rates for two loops using the historical data.
5. Estimate the no-arbitrage bounds based on the historical log rates.
6. Calculate the current log rates using the latest bid and ask prices.
7. Check for arbitrage opportunities by comparing the current log rates with the no-arbitrage bounds.

The output of the project provides the no-arbitrage bounds for both loops and indicates whether there are any arbitrage opportunities for each loop. If the current log rate for a loop is outside the no-arbitrage bounds, it suggests a potential arbitrage opportunity.

## Testing

The test_project.py file is organized into three test classes, each corresponding to a module in your project:

1.  **TestBinanceAPI**: This class contains test cases for the functions in the `binance_api.py` module. It tests the `get_binance_data`, `fetch_prices`, and `fetch_historical_data` functions to ensure they fetch the correct data from the Binance API.

2.  **TestDataProcessing**: This class contains test cases for the functions in the `data_processing.py` module. It tests the `convert_to_log` and `parse_historical_data` functions to ensure they correctly process the fetched data.

3.  **TestArbitrageAnalysis**: This class contains test cases for the functions in the `arbitrage_analysis.py` module. It tests the `calculate_log_rates`, `check_arbitrage_opportunities`, `calculate_historical_log_rates`, and `estimate_no_arbitrage_bounds` functions to ensure they correctly analyze the processed data and identify arbitrage opportunities.

Each test case in these classes checks if the corresponding function produces the expected output for a given input. The test cases cover various scenarios, including different data samples, invalid inputs, and edge cases. The tests help ensure that your code is reliable, robust, and efficient.

To run the tests, execute the following command:

`python test_project.py`
