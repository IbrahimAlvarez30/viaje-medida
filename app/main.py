from flask import Flask
from data.data_destiny import data
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/destination")
def destinations():
    return render_template("destination.html")
