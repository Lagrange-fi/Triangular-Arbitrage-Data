import os
import secrets
from flask import Flask, render_template, request, flash
import main

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
            results = main.run_analysis(currency_pairs)
        else:
            flash('Invalid currency pairs. Please provide pairs that can form two different triangular arbitrages with two different FIAT currencies and BTC.', 'danger')
    return render_template('index.html', results=results)

def validate_currency_pairs(currency_pairs):
    fiat_currencies = set()
    btc_pairs = set()

    for pair in currency_pairs:
        if 'BTC' in pair:
            btc_pairs.add(pair)
            fiat_currencies.add(pair.replace('BTC', ''))

    return len(fiat_currencies) == 3 and len(btc_pairs) == 3

if __name__ == '__main__':
    app.run(debug=True)