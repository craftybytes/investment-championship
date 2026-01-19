from flask import Flask, render_template, request, redirect, url_for, flash
import random
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    search_query = request.args.get('search', '')
    return render_template("about.html", search_query=search_query)


@app.route("/information")
def information():
    return render_template("information.html")


@app.route("/rules", methods=['GET', 'POST'])
def rules():
    return render_template("rules.html")

@app.route("/timeline")
def timeline():
    return render_template("timeline.html")


if __name__ == '__main__':
    app.run(debug=True, port=5001)