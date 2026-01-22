from flask import Flask, render_template, request, redirect, url_for
import yfinance
from flask import jsonify
from datetime import datetime
import os

# To-do:
"""
- make moving timer for deadlines and important times
"""

app = Flask(__name__)


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


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html')


@app.route("/api/stock/<symbol>")
def get_stock(symbol):
    try:
        stock = yfinance.Ticker(symbol)
        hist = stock.history(period="2d")

        if hist.empty:
            return jsonify({'error': 'No data available'}), 404

        current_price = hist['Close'].iloc[-1]

        if len(hist) > 1:
            previous_close = hist['Close'].iloc[-2]
        else:
            info = stock.info
            previous_close = info.get('previousClose', current_price)

        change = current_price - previous_close
        change_percent = (change / previous_close) * 100 if previous_close != 0 else 0

        info = stock.info
        company_name = info.get('longName') or info.get('shortName') or f"{symbol} Corporation"

        return jsonify({
            'symbol': symbol,
            'name': company_name,
            'price': float(current_price),
            'change': float(change),
            'change_percent': float(change_percent)
        })
    except Exception as e:
        print(f"Error fetching {symbol}: {str(e)}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)