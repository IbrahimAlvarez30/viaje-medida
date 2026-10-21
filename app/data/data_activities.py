activities = [
    {
        "id": 1,
        "name": "Ceremonia del Té en Gion",
        "destination_id": 1,
        "duration_hours": 2,
        "price_per_person": 30,
        "included_items": ["Degustación de dulces tradicionales matcha"],
    },
    {
        "id": 2,
        "name": "Tour Nocturno por Fushimi Inari",
        "destination_id": 1,
        "duration_hours": 3,
        "price_per_person": 40,
        "physical_difficulty": "media",
        "minimum_age": 10,
    },
    {
        "id": 3,
        "name": "Clase de Cocina Ramen y Gyozas",
        "destination_id": 1,
        "duration_hours": 3,
        "price_per_person": 65,
        "minimum_age": 12,
        "included_items": ["Todos los ingredientes", "Delantal", "Recetario impreso"],
    },
    {
        "id": 4,
        "name": "Ruta en Bicicleta por el Bosque de Bambú",
        "destination_id": 1,
        "duration_hours": 4,
        "price_per_person": 50,
        "physical_difficulty": "baja",
        "included_items": ["Alquiler de bicicleta eléctrica", "Casco"],
    },
    {
        "id": 5,
        "name": "Ruta de las Especias y Paseo en Dhow",
        "destination_id": 3,
        "duration_hours": 5,
        "price_per_person": 45,
        "physical_difficulty": "baja",
        "included_items": ["Almuerzo tradicional especiado"],
    },
    {
        "id": 6,
        "name": "Snorkel en el Atolón Mnemba",
        "destination_id": 3,
        "duration_hours": 4,
        "price_per_person": 60,
        "physical_difficulty": "media",
        "minimum_age": 8,
        "included_items": ["Tubo", "Gafas", "Aletas"],
    },
    {
        "id": 7,
        "name": "Visita Guiada por Stone Town",
        "destination_id": 3,
        "duration_hours": 2,
        "price_per_person": 20,
    },
    {
        "id": 8,
        "name": "Buceo en Cenotes Sagrados",
        "destination_id": 4,
        "duration_hours": 4,
        "price_per_person": 75,
        "physical_difficulty": "alta",
        "minimum_age": 16,
        "included_items": [
            "Bombona de oxígeno",
            "Linterna subacuática",
            "Traje de neopreno",
        ],
    },
    {
        "id": 9,
        "name": "Excursión a las Ruinas de Tulum",
        "destination_id": 4,
        "duration_hours": 6,
        "price_per_person": 55,
        "physical_difficulty": "baja",
        "included_items": ["Entradas al recinto arqueológico", "Transporte en autobús"],
    },
    {
        "id": 10,
        "name": "Paseo en Catamarán al Atardecer",
        "destination_id": 4,
        "duration_hours": 3,
        "price_per_person": 65,
        "minimum_age": 18,
        "included_items": ["Barra libre de bebidas", "Aperitivos a bordo"],
    },
]


def contar_actividades():
    return len(activities)


def obtener_actividades():
    return activities


def obtener_actividad_por_id(act_id):
    for item in activities:
        if item["id"] == act_id:
            return item
    return None


def obtener_actividades_por_destino(destino_id):
    return [item for item in activities if item["destination_id"] == destino_id]
