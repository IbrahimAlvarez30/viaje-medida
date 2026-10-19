from flask import Flask, render_template, request
from data.data_destinations import contar_destinos, destinations, filtrar_destinos
from data.data_accommodations import (
    contar_alojamientos,
    accommodations,
    filtrar_alojamientos,
)
from data.data_activities import contar_actividades
from forms import (
    ExploradorDestinosForm,
    ComparadorAlojamientosForm,
    AsistenteViajeMedidaForm,
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


# Función para el Asistente "Viaje a Medida"
def buscar_viaje_a_medida(
    destinos,
    alojamientos,
    entorno=None,
    sin_visado=False,
    tipo_alojamiento=None,
    precio_max=None,
    desayuno=False,
):
    combinaciones_validas = []
    destinos_filtrados = filtrar_destinos(
        destinos, entorno=entorno, sin_visado=sin_visado
    )
    ids_destinos_validos = {d["id"]: d for d in destinos_filtrados}

    for a in alojamientos:
        destino = ids_destinos_validos.get(a.get("destino_id"))
        if not destino:
            continue
        if precio_max is not None and a.get("precio_noche", 0) > precio_max:
            continue
        if tipo_alojamiento and a.get("tipo") != tipo_alojamiento:
            continue
        if desayuno and not a.get("desayuno", False):
            continue

        combinaciones_validas.append({"destino": destino, "alojamiento": a})

    return combinaciones_validas


# Ruta: Explorador de Destinos
@app.route("/buscar/destinos", methods=["GET"])
def explorador_destinos():
    form = ExploradorDestinosForm(request.args)
    if form.validate():
        resultados = filtrar_destinos(
            destinations, form.entorno.data, form.sin_visado.data
        )
    else:
        resultados = destinations
    return render_template("explorador_destinos.html", form=form, resultados=resultados)


# Ruta: Comparador de Alojamientos
@app.route("/buscar/alojamientos", methods=["GET"])
def comparador_alojamientos():
    form = ComparadorAlojamientosForm(request.args)
    if form.validate():
        resultados = filtrar_alojamientos(
            accommodations,
            form.precio_max.data,
            form.tipo.data,
            form.desayuno.data,
            form.mascotas.data,
        )
    else:
        resultados = accommodations
    return render_template(
        "comparador_alojamientos.html", form=form, resultados=resultados
    )


# Ruta: Asistente Viaje a Medida
@app.route("/buscar/viaje-a-medida", methods=["GET"])
def viaje_a_medida():
    form = AsistenteViajeMedidaForm(request.args)
    combinaciones = []
    busqueda_realizada = False

    if form.validate() and request.args:
        busqueda_realizada = True
        combinaciones = buscar_viaje_a_medida(
            destinos=destinations,
            alojamientos=accommodations,
            entorno=form.entorno.data,
            sin_visado=form.sin_visado.data,
            tipo_alojamiento=form.tipo_alojamiento.data,
            precio_max=form.precio_max.data,
            desayuno=form.desayuno.data,
        )

    return render_template(
        "viaje_medida.html",
        form=form,
        combinaciones=combinaciones,
        busqueda_realizada=busqueda_realizada,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
