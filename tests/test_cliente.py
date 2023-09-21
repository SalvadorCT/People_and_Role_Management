import pytest
from src.personas.cliente import Cliente


# Define la función de prueba parametrizada y los casos de prueba
@pytest.mark.parametrize(
    "identificacion, nombre, apellido, direccionfiscal, codepostal, estado",
    [
        ("123456", "Juan", "Perez", "1234 Elm Street", "90210", "Soltero"),
        ("789012", "Ana", "Gomez", "567 Main St", "30318", "Casado"),
        ("456789", "Pedro", "Lopez", "890 Oak Avenue", "10001", "Divorciado"),
        ("111111", "María", "Sánchez", "432 Pine Road", "60601", "Casado"),
        ("222222", "Luis", "Rodríguez", "789 Maple Lane", "90210", "Soltero"),
        ("333333", "Laura", "Martínez", "987 Cedar Street", "30318", "Viudo"),
    ]
)
def test_creacion_estudiante(
        identificacion, nombre, apellido, direccionfiscal, codepostal, estado
):
    # Prueba de creación de un estudiante
    estudiante = Cliente(
        id=identificacion,
        nombre=nombre,
        apellido=apellido,
        direccion_fiscal=direccionfiscal,
        codigo_postal=codepostal,
        estado=estado,
    )

    assert estudiante.id == identificacion
    assert estudiante.nombre == nombre
    assert estudiante.apellido == apellido
    assert estudiante.direccion_fiscal == direccionfiscal
    assert estudiante.codigo_postal == codepostal
    assert estudiante.estado == estado
