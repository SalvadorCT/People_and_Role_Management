import pytest
from src.personas.estudiante import Estudiante


# Define la función de prueba parametrizada y los casos de prueba
@pytest.mark.parametrize(
    "identificacion, nombre, apellido, semestre",
    [
        ("123456", "Juan", "Perez", 3),
        ("789012", "Ana", "Gomez", 4),
        ("456789", "Pedro", "Lopez", 2),
        ("111111", "María", "Sánchez", 1),
        ("222222", "Luis", "Rodríguez", 5),
        ("333333", "Laura", "Martínez", 2),
    ]
)
def test_creacion_estudiante(identificacion, nombre, apellido, semestre):
    estudiante = Estudiante(
        id=identificacion,
        nombre=nombre,
        apellido=apellido,
        semestre_matricula=semestre
    )

    # Obtener la representación de cadena del objeto
    cadena_estudiante = str(estudiante)

    # Datos Esperados
    assert estudiante.id == identificacion
    assert estudiante.nombre == nombre
    assert estudiante.apellido == apellido
    assert estudiante.semestre_matricula == semestre
    assert print(estudiante) is None
    assert estudiante.adicional_info() is None
    assert cadena_estudiante == (f'\nHola! soy un Estudiante...'
                                 f'\n🆔 Identificacion: {estudiante.id}'
                                 f'\n👤 Nombre: {estudiante.nombre} {estudiante.apellido}'
                                 f'\n📚 Semestre de Matricula: {estudiante.semestre_matricula}')
