from src.personas.empleado import Empleado


def test_empleado():
    empleado = Empleado('12345678',
                        'Juan',
                        'Perez',
                        ' 1234',
                        "administrador", 1000)

    assert empleado.id == '12345678'
    assert empleado.nombre == 'Juan'
    assert empleado.apellido == 'Perez'
    assert empleado.fecha_ingreso == ' 1234'
    assert empleado.cargo == "administrador"
    assert print(empleado) is None
    assert empleado.__str__() == (f'\nHola! soy un Empleado...'
                                  f'\n🆔 Identificacion es: 12345678'
                                  f'\n👤 Nombre: Juan Perez'
                                  f'\n📅 Fecha de ingreso:  1234'
                                  f'\n💼 Cargo: administrador'
                                  f'\n💰 Sueldo Mensual: $1000')

    assert empleado.adicional_info() is None
