destinations = [
    {
        "id": 1,
        "name": "Kioto",
        "country": "Japón",
        "environment": "ciudad",
        "high_season": "primavera",
        "visa_required": False,
        "additional_advice": "La moneda local es el yen y recomendamos llevar siempre efectivo para el acceso a los templos tradicionales.",
    },
    {
        "id": 2,
        "name": "Islas Lofoten",
        "country": "Noruega",
        "environment": "montaña",
        "high_season": "invierno",
        "visa_required": False,
        "additional_advice": "Es imprescindible viajar con ropa térmica extrema y calzado impermeable.",
    },
    {
        "id": 3,
        "name": "Zanzíbar",
        "country": "Tanzania",
        "environment": "playa",
        "high_season": "verano",
        "visa_required": True,
    },
    {
        "id": 4,
        "name": "Playa del Carmen",
        "country": "México",
        "environment": "playa",
        "high_season": "verano",
        "visa_required": False,
        "additional_advice": "La moneda es el peso mexicano, aunque aceptan dólares en casi todas las zonas turísticas.",
    },
]


def contar_destinos():
    return len(destinations)


# Función para el Explorador de Destinos
def filtrar_destinos(destinos, entorno=None, sin_visado=False):
    resultados = []
    for d in destinos:
        if entorno and d.get("entorno") != entorno:
            continue
        if (
            sin_visado and d.get("requiere_visado") is True
        ):  # Si requiere visado, se omite
            continue
        resultados.append(d)
    return resultados
