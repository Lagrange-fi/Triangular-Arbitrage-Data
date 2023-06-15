# Cryptocurrency Arbitrage Analysis

This project aims to identify potential arbitrage opportunities in the cryptocurrency market by analyzing price data from the Binance exchange. The analysis focuses on five currency pairs: BTCUSDT, EURUSDT, BTCEUR, USDTTRY, and BTCTRY. The project consists of four Python files: `binance_api.py`, `data_processing.py`, `main.py`, and `arbitrage_analysis.py`.

## Key Components

1. **Data Collection**: The `binance_api.py` file contains functions to fetch the latest bid and ask prices and historical data for the selected currency pairs using the Binance API.

2. **Data Processing**: The `data_processing.py` file processes the fetched data by converting bid and ask prices to their logarithmic form and parsing the historical data to extract relevant information.

3. **Arbitrage Analysis**: The `arbitrage_analysis.py` file contains functions to calculate log rates, historical log rates, estimate no-arbitrage bounds, and check for arbitrage opportunities.

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
