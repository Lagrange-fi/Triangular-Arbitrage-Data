# Triangular Arbitrage Analysis

This project aims to identify potential arbitrage opportunities in the cryptocurrency market by analyzing price data from the Binance exchange. The analysis mainly focused on five currency pairs: BTCUSDT, EURUSDT, BTCEUR, USDTTRY, and BTCTRY. Users can now change these pairs via the UI. The project consists of four Python files: `binance_api.py`, `data_processing.py`, `main.py`, and `arbitrage_analysis.py`.

## Getting Started

Before running the project, make sure to install the required dependencies. You can do this by running the following command in your terminal or command prompt:
`pip install -r requirements.txt`
This will install the necessary packages listed in the `requirements.txt` file.
Then run `python3 app.py` and head to: `http://127.0.0.1:5000`

## Key Components

1. **Data Collection**: The `binance_api.py` file contains functions to fetch the latest bid and ask prices and historical data for the selected currency pairs using the Binance API.

2. **Data Processing**: The `data_processing.py` file processes the fetched data by converting bid and ask prices to their logarithmic form and parsing the historical data to extract relevant information.

3. **Arbitrage Analysis**: The `arbitrage_analysis.py` file contains functions to calculate log rates, historical log rates, estimate no-arbitrage bounds, and check for arbitrage opportunities.

4. **Main Script**: The `main.py` file is the main script that combines the functions from the other files to perform the complete analysis. It fetches and processes the data, calculates historical log rates, estimates no-arbitrage bounds, and checks for arbitrage opportunities.

5. **Web Application**: The `app.py` file is the Flask web application that provides a user interface for users to input currency pairs, validates the provided currency pairs to ensure they are available in the Binance API and can form two different triangular arbitrages and view the results of the arbitrage analysis. It uses the `main.py` script to run the analysis based on the user's input.

6. **HTML Templates**: The `templates` folder contains the HTML templates for the web application. The `base.html` file is the base template that includes the common structure and styling, while the `index.html` file extends the base template and contains the content specific to the main page, including the form for inputting currency pairs and displaying the results of the analysis.

7. **Testing**: The `test_project.py` file is for testing the algorithm. Read below for more information.

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

The `test_project.py` file is organized into three test classes, each corresponding to a module in your project:

1.  **TestBinanceAPI**: This class contains test cases for the functions in the `binance_api.py` module. It tests the `get_binance_data`, `fetch_prices`, and `fetch_historical_data` functions to ensure they fetch the correct data from the Binance API.

2.  **TestDataProcessing**: This class contains test cases for the functions in the `data_processing.py` module. It tests the `convert_to_log` and `parse_historical_data` functions to ensure they correctly process the fetched data.

3.  **TestArbitrageAnalysis**: This class contains test cases for the functions in the `arbitrage_analysis.py` module. It tests the `calculate_log_rates`, `check_arbitrage_opportunities`, `calculate_historical_log_rates`, and `estimate_no_arbitrage_bounds` functions to ensure they correctly analyze the processed data and identify arbitrage opportunities.

Each test case in these classes checks if the corresponding function produces the expected output for a given input. The test cases cover various scenarios, including different data samples, invalid inputs, and edge cases. The tests help ensure that your code is reliable, robust, and efficient.

To run the tests, execute the following command:

`python test_project.py`

## User Interface

The application features a user-friendly web interface that allows users to input currency pairs for triangular arbitrage analysis. Users can provide 6 currency pairs that form two different triangular arbitrages with two different FIAT currencies and BTC. The default currency pairs are shown in the page.


Once the user submits valid currency pairs, the application runs the arbitrage analysis and displays the results, including no-arbitrage bounds and arbitrage opportunities.
