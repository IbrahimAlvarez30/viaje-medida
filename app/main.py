from flask import Flask, render_template
from data.data_destinations import contar_destinos
from data.data_accommodations import contar_alojamientos
from data.data_activities import contar_actividades

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template(
        "inicio.html",
        total_destinos=contar_destinos(),
        total_alojamientos=contar_alojamientos(),
        total_actividades=contar_actividades(),
    )


@app.route("/acerca")
def acerca():
    return render_template("acerca.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
