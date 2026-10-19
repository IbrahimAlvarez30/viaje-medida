from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Optional, NumberRange


class ExploradorDestinosForm(FlaskForm):
    class Meta:
        csrf = False  # Desactivar CSRF para formularios de solo consulta

    entorno = SelectField(
        "Entorno",
        choices=[
            ("", "Todos los entornos"),
            ("playa", "Playa"),
            ("montaña", "Montaña"),
            ("ciudad", "Ciudad"),
        ],
        validators=[Optional()],
    )

    sin_visado = BooleanField("Sin visado previo")


class ComparadorAlojamientosForm(FlaskForm):
    class Meta:
        csrf = False

    precio_max = IntegerField(
        "Presupuesto máximo por noche (€)",
        validators=[
            Optional(),
            NumberRange(min=0, message="El precio no puede ser negativo"),
        ],
    )
    tipo = SelectField(
        "Tipo de alojamiento",
        choices=[
            ("", "Todos los tipos"),
            ("hotel", "Hotel"),
            ("hostal", "Hostal"),
            ("cabaña", "Cabaña"),
            ("apartamento", "Apartamento"),
        ],
        validators=[Optional()],
    )

    desayuno = BooleanField("Desayuno incluido")
    mascotas = BooleanField("Admite mascotas")


class AsistenteViajeMedidaForm(FlaskForm):
    class Meta:
        csrf = False

    # Filtros de Destino
    entorno = SelectField(
        "Entorno deseado",
        choices=[
            ("", "Todos los entornos"),
            ("playa", "Playa"),
            ("montaña", "Montaña"),
            ("ciudad", "Ciudad"),
        ],
        validators=[Optional()],
    )
    sin_visado = BooleanField("Sin visado previo")

    # Filtros de Alojamiento
    tipo_alojamiento = SelectField(
        "Tipo de alojamiento",
        choices=[
            ("", "Todos los tipos"),
            ("hotel", "Hotel"),
            ("hostal", "Hostal"),
            ("cabaña", "Cabaña"),
            ("apartamento", "Apartamento"),
        ],
        validators=[Optional()],
    )
    precio_max = IntegerField(
        "Gasto máximo por noche (€)",
        validators=[
            Optional(),
            NumberRange(min=0, message="El precio no puede ser negativo"),
        ],
    )
    desayuno = BooleanField("Requiere desayuno incluido")
