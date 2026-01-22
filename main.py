from flask import Flask, render_template, session, jsonify
import yfinance as yf
from datetime import datetime
import os
import time

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Default stocks for new users
DEFAULT_STOCKS = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN', 'NVDA', 'META', 'NFLX']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/rules')
def rules():
    return render_template('rules.html')


@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


if __name__ == '__main__':
    app.run(debug=True)