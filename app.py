import os
import secrets
from flask import Flask, render_template, request, flash
import main
from binance_api import fetch_available_pairs
import asyncio

app = Flask(__name__)
app.secret_key = secrets.token_hex(16) # Generates a random 32-character-long hexadecimal string

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        currency_pairs = [
            request.form['currency_pair_1'],
            request.form['currency_pair_2'],
            request.form['currency_pair_3'],
            request.form['currency_pair_4'],
            request.form['currency_pair_5'],
            request.form['currency_pair_6']
        ]
        if validate_currency_pairs(currency_pairs):
            results = asyncio.run(main.run_analysis(currency_pairs))
    return render_template('index.html', results=results)

def validate_currency_pairs(currency_pairs):
    available_pairs = fetch_available_pairs()
    fiat_currencies = set()
    btc_pairs = set()

    for pair in currency_pairs:
        if pair not in available_pairs:
            flash(f"Invalid currency pair: {pair}. Please provide pairs available in the Binance API.", "danger")
            return False

        if 'BTC' in pair:
            btc_pairs.add(pair)
            fiat_currencies.add(pair.replace('BTC', ''))

    if len(fiat_currencies) != 3 or len(btc_pairs) != 3:
        flash("Please provide pairs that can form two different triangular arbitrages with two different FIAT currencies and BTC.", "danger")
        return False

    return True

if __name__ == '__main__':
    app.run(debug=True)