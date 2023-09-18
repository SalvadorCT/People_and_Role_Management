import unittest
from src.personas.persona import Persona


def testPersona():
    persona = Persona('12345678',
                      'Juan',
                      'Perez')

    assert persona.id == '12345678'
    assert persona.nombre == 'Juan'
    assert persona.apellido == 'Perez'
    assert print(persona) is None
    assert persona.__str__() == (f'\nHola! soy una Persona...'
                                 f'\n🆔 Identificacion: 12345678'
                                 f'\n👤 Nombre: Juan Perez')
    assert persona.adicional_info() is None


class MyTestCase(unittest.TestCase):  # Funciona como un contenedor de pruebas a futuro
    pass


if __name__ == '__main__':
    unittest.main()
