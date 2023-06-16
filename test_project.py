import unittest
from binance_api import get_binance_data, fetch_prices, fetch_historical_data
from data_processing import convert_to_log, parse_historical_data
from arbitrage_analysis import calculate_log_rates, check_arbitrage_opportunities, calculate_historical_log_rates, estimate_no_arbitrage_bounds

class TestBinanceAPI(unittest.TestCase):
    def test_get_binance_data(self):
        # Test case for get_binance_data function
        symbol = 'BTCUSDT'
        data = get_binance_data(symbol)
        self.assertIsNotNone(data)
        self.assertIn('bidPrice', data)
        self.assertIn('askPrice', data)

    def test_fetch_prices(self):
        # Test case for fetch_prices function
        currency_pairs = ['BTCUSDT']
        prices = fetch_prices(currency_pairs)
        self.assertIsNotNone(prices)
        self.assertIn('BTCUSDT', prices)

    def test_fetch_historical_data(self):
        # Test case for fetch_historical_data function
        symbol = 'BTCUSDT'
        data = fetch_historical_data(symbol)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)

class TestDataProcessing(unittest.TestCase):
    def test_convert_to_log(self):
        # Test case for convert_to_log function
        prices = {'BTCUSDT': {'bid': '10000', 'ask': '10001'}}
        expected_result = {'BTCUSDT': {'bid_log': 9.210340371976184, 'ask_log': 9.21044003427029}}
        result = convert_to_log(prices)
        self.assertAlmostEqual(result['BTCUSDT']['bid_log'], expected_result['BTCUSDT']['bid_log'], places=6)
        self.assertAlmostEqual(result['BTCUSDT']['ask_log'], expected_result['BTCUSDT']['ask_log'], places=6)

    def test_parse_historical_data(self):
        # Test case for parse_historical_data function
        data = [
            [1623770400000, "10000.00000000", "10001.00000000", "9999.00000000", "10000.00000000", "0.00100000", 1623773999999, "10.00000000", 1, "0.00100000", "10.00000000", "0"]
        ]
        parsed_data = parse_historical_data(data)
        self.assertIsNotNone(parsed_data)
        self.assertIsInstance(parsed_data, list)
        self.assertEqual(len(parsed_data), 1)
        self.assertIn('timestamp', parsed_data[0])
        self.assertIn('open', parsed_data[0])
        self.assertIn('high', parsed_data[0])
        self.assertIn('low', parsed_data[0])
        self.assertIn('close', parsed_data[0])

class TestArbitrageAnalysis(unittest.TestCase):
    def test_calculate_log_rates(self):
        # Test case for calculate_log_rates function
        log_prices = {
            'BTCUSDT': {'ask_log': 9.21044003427029, 'bid_log': 9.210340371976184},
            'BTCEUR': {'ask_log': 8.987196820661973, 'bid_log': 8.987096158367867},
            'EURUSDT': {'ask_log': 0.1823215567939546, 'bid_log': 0.1822218944998485},
            'USDTTRY': {'ask_log': 2.1400661634962708, 'bid_log': 2.1399665012021647},
            'BTCTRY': {'ask_log': 11.350506534672205, 'bid_log': 11.350406872378099}
        }
        log_rates = calculate_log_rates(log_prices)
        self.assertIsNotNone(log_rates)
        self.assertIn('loop1', log_rates)
        self.assertIn('loop2', log_rates)

    def test_check_arbitrage_opportunities(self):
        # Test case for check_arbitrage_opportunities function
        log_rates = {'loop1': 0, 'loop2': 0}
        no_arbitrage_bounds = {'loop1': {'upper': 1, 'lower': -1}, 'loop2': {'upper': 1, 'lower': -1}}
        opportunities = check_arbitrage_opportunities(log_rates, no_arbitrage_bounds)
        self.assertIsNotNone(opportunities)
        self.assertIn('loop1', opportunities)
        self.assertIn('loop2', opportunities)

    def test_calculate_historical_log_rates(self):
        # Test case for calculate_historical_log_rates function
        sample_parsed_historical_data = {
            'BTCUSDT': [{'close': 10000.0}],
            'EURUSDT': [{'close': 1.2}],
            'BTCEUR': [{'close': 8000.0}],
            'USDTTRY': [{'close': 8.5}],
            'BTCTRY': [{'close': 85000.0}]
        }
        historical_log_rates = calculate_historical_log_rates(sample_parsed_historical_data)
        self.assertIsNotNone(historical_log_rates)
        self.assertIn('loop1', historical_log_rates)
        self.assertIn('loop2', historical_log_rates)
        self.assertEqual(len(historical_log_rates['loop1']), 1)
        self.assertEqual(len(historical_log_rates['loop2']), 1)

    def test_estimate_no_arbitrage_bounds(self):
        # Test case for estimate_no_arbitrage_bounds function
        historical_log_rates = {'loop1': [0, 0.5, 1, -0.5, -1], 'loop2': [0, 0.5, 1, -0.5, -1]}
        no_arbitrage_bounds = estimate_no_arbitrage_bounds(historical_log_rates)
        self.assertIsNotNone(no_arbitrage_bounds)
        self.assertIn('loop1', no_arbitrage_bounds)
        self.assertIn('loop2', no_arbitrage_bounds)
        self.assertIn('upper', no_arbitrage_bounds['loop1'])
        self.assertIn('lower', no_arbitrage_bounds['loop1'])
        self.assertIn('upper', no_arbitrage_bounds['loop2'])
        self.assertIn('lower', no_arbitrage_bounds['loop2'])

if __name__ == '__main__':
    unittest.main()