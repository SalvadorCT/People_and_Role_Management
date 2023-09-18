from src.personas.estudiante import Estudiante


def test_estudiante():
    estudiante = Estudiante('12345678',
                            'Juan',
                            'Perez',
                            2)

    assert estudiante.id == '12345678'
    assert estudiante.nombre == 'Juan'
    assert estudiante.apellido == 'Perez'
    assert estudiante.semestre_matricula == 2
    assert print(estudiante) is None
    assert estudiante.__str__() == (f'\nHola! soy un Estudiante...'
                                    f'\n🆔 Identificacion: 12345678'
                                    f'\n👤 Nombre: Juan Perez'
                                    f'\n📚 Semestre de Matricula: 2')