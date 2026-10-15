from data.data_destinations import destinations
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


"""
@app.route("/destination")
def destinations_page():
    return render_template("destination.html", destiantions=destinations)
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
