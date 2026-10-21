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


def obtener_destinos():
    return destinations


def obtener_destino_por_id(destino_id):
    for item in destinations:
        if item["id"] == destino_id:
            return item
    return None
