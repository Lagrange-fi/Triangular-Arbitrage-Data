#!/bin/bash

set -e

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
pip install gunicorn

# Move Flask app files to be served by Gunicorn
rm -rf build
mkdir build
cp -r templates build/templates
cp -r static build/static
cp app.py build/
cp main.py build/
cp arbitrage_analysis.py build/
cp binance_api.py build/

# Run Gunicorn to create a server
cd build
gunicorn app:app -b 0.0.0.0:8000 -D