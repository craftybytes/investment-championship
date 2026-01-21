from flask import Flask, render_template, request, redirect, url_for
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


if __name__ == '__main__':
    app.run(debug=True)