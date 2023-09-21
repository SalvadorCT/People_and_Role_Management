import pytest
from src.personas.persona import Persona


@pytest.mark.parametrize(
    "identificacion, nombre, apellido",
    [
        ('123456', 'Juan', 'Perez'),
        ('876543', 'Maria', 'Gonzalez'),
        ('555555', 'Pedro', 'Lopez'),
        ('999999', 'Laura', 'Martinez'),
        ('111111', 'Sara', 'Fernandez'),
    ]
)
def test_persona(identificacion, nombre, apellido):
    # Prueba de creación de la clase Persona
    persona = Persona(
        id=identificacion,
        nombre=nombre,
        apellido=apellido,
    )

    # Obtener la representación de cadena del objeto
    cadena_persona = str(persona)

    assert persona.id == identificacion
    assert persona.nombre == nombre
    assert persona.apellido == apellido
    assert print(persona) is None
    assert persona.adicional_info() is None
    assert cadena_persona == (f'\nHola! soy una Persona...'
                              f'\n🆔 Identificacion: {persona.id}'
                              f'\n👤 Nombre: {persona.nombre} {persona.apellido}')

# class MyTestCase(unittest.TestCase):  # Funciona como un contenedor de pruebas a futuro
#     pass
