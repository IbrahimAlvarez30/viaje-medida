accommodations = [
    {
        "id": 1,
        "name": "Ryokan Tradicional Gion",
        "destination_id": 1,
        "type": "hotel",
        "price_per_night": 140,
        "breakfast_included": True,
        "pets_allowed": False,
        "stars": 4,
        "additional_services": "Baño termal privado en la habitación",
    },
    {
        "id": 2,
        "name": "Capsule Hostel Urban",
        "destination_id": 1,
        "type": "hostal",
        "price_per_night": 35,
        "breakfast_included": False,
        "pets_allowed": False,
        "stars": 2,
    },
    {
        "id": 3,
        "name": "Apartamento Bambú Arashiyama",
        "destination_id": 1,
        "type": "apartamento",
        "price_per_night": 95,
        "breakfast_included": False,
        "pets_allowed": True,
        "additional_services": "Terraza con vistas al río",
    },
    {
        "id": 4,
        "name": "Rorbu Fjord Cabins",
        "destination_id": 2,
        "type": "cabaña",
        "price_per_night": 160,
        "breakfast_included": True,
        "pets_allowed": True,
        "stars": 4,
        "additional_services": "Acceso directo al muelle del fiordo",
    },
    {
        "id": 5,
        "name": "Arctic Light Hotel",
        "destination_id": 2,
        "type": "hotel",
        "price_per_night": 210,
        "breakfast_included": True,
        "pets_allowed": False,
        "stars": 5,
        "additional_services": "Mirador acristalado en la azotea",
    },
    {
        "id": 6,
        "name": "Refugio de Pescadores Svolvær",
        "destination_id": 2,
        "type": "hostal",
        "price_per_night": 55,
        "breakfast_included": False,
        "pets_allowed": True,
    },
    {
        "id": 7,
        "name": "Hostal Caribe Maya",
        "destination_id": 4,
        "type": "hostal",
        "price_per_night": 25,
        "breakfast_included": True,
        "pets_allowed": True,
        "stars": 2,
    },
    {
        "id": 8,
        "name": "Eco-Villas Tulum Road",
        "destination_id": 4,
        "type": "cabaña",
        "price_per_night": 110,
        "breakfast_included": False,
        "pets_allowed": True,
        "stars": 3,
        "additional_services": "Funciona con energía solar",
    },
    {
        "id": 9,
        "name": "Grand Resort Riviera",
        "destination_id": 4,
        "type": "hotel",
        "price_per_night": 190,
        "breakfast_included": True,
        "pets_allowed": False,
        "stars": 5,
        "additional_services": "Club de playa privado",
    },
    {
        "id": 10,
        "name": "Loft Quinta Avenida",
        "destination_id": 4,
        "type": "apartamento",
        "price_per_night": 80,
        "breakfast_included": False,
        "pets_allowed": False,
    },
]


def contar_alojamientos():
    return len(accommodations)


# Función para el Comparador de Alojamientos
def filtrar_alojamientos(
    alojamientos, precio_max=None, tipo=None, desayuno=False, mascotas=False
):
    resultados = []
    for a in alojamientos:
        if precio_max is not None and a.get("precio_noche", 0) > precio_max:
            continue
        if tipo and a.get("tipo") != tipo:
            continue
        if desayuno and not a.get("desayuno", False):
            continue
        if mascotas and not a.get("mascotas", False):
            continue
        resultados.append(a)
    return resultados
