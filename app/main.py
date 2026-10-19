from flask import Flask, render_template
from data.data_destinations import (
    contar_destinos,
    obtener_destinos,
    obtener_destino_por_id,
)
from data.data_accommodations import (
    contar_alojamientos,
    obtener_alojamientos,
    obtener_alojamiento_por_id,
    obtener_alojamientos_por_destino,
)
from data.data_activities import (
    contar_actividades,
    obtener_actividades,
    obtener_actividad_por_id,
    obtener_actividades_por_destino,
)

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


@app.route("/destinos")
def listado_destinos():
    return render_template("destinos.html", destinos=obtener_destinos())


@app.route("/alojamientos")
def listado_alojamientos():
    return render_template("alojamientos.html", alojamientos=obtener_alojamientos())


@app.route("/actividades")
def listado_actividades():
    actividades = obtener_actividades()
    actividades_con_destino = []
    for act in actividades:
        destino = obtener_destino_por_id(act["destination_id"])
        actividades_con_destino.append(
            {
                "id": act["id"],
                "name": act["name"],
                "destination_name": destino["name"] if destino else "Desconocido",
            }
        )
    return render_template("actividades.html", actividades=actividades_con_destino)


@app.route("/destino/<int:destino_id>")
def detalle_destino(destino_id):
    destino = obtener_destino_por_id(destino_id)
    alojamientos = obtener_alojamientos_por_destino(destino_id)
    actividades = obtener_actividades_por_destino(destino_id)

    return render_template(
        "destino_detalle.html",
        destino=destino,
        alojamientos=alojamientos,
        actividades=actividades,
    )


@app.route("/alojamiento/<int:alojamiento_id>")
def detalle_alojamiento(alojamiento_id):
    alojamiento = obtener_alojamiento_por_id(alojamiento_id)
    destino = obtener_destino_por_id(alojamiento["destination_id"])
    return render_template(
        "alojamiento_detalle.html", alojamiento=alojamiento, destino=destino
    )


@app.route("/actividad/<int:actividad_id>")
def detalle_actividad(actividad_id):
    actividad = obtener_actividad_por_id(actividad_id)
    destino = obtener_destino_por_id(actividad["destination_id"])
    return render_template(
        "actividad_detalle.html", actividad=actividad, destino=destino
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
