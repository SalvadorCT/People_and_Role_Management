import pytest
from src.personas.empleado import Empleado


@pytest.mark.parametrize(
    "identificacion, nombre, apellido, fechaingreso, cargo, sueldo",
    [
        ('123456', 'Juan', 'Perez', '1234', 'administrador', 1000),
        ('876543', 'Maria', 'Gonzalez', '5678', 'analista', 3000),
        ('555555', 'Pedro', 'Lopez', '9999', 'desarrollador', 4000),
        ('999999', 'Laura', 'Martinez', '7777', 'gerente', 6000),
        ('111111', 'Sara', 'Fernandez', '8888', 'diseñador', 3500),
    ]
)
def test_creacion_empleado(identificacion, nombre, apellido, fechaingreso, cargo, sueldo):
    # Prueba de creación de un empleado
    empleado = Empleado(
        id=identificacion, 
        nombre=nombre, 
        apellido=apellido, 
        fecha_ingreso=fechaingreso, 
        cargo=cargo,
        sueldo=sueldo
        )
    
    # Obtener la representación de cadena del objeto
    cadena_empleado = str(empleado)

    assert empleado.id == identificacion
    assert empleado.nombre == nombre
    assert empleado.apellido == apellido
    assert empleado.fecha_ingreso == fechaingreso
    assert empleado.cargo == cargo
    assert empleado.sueldo == sueldo
    assert print(empleado) is None
    assert empleado.adicional_info() is None
    assert cadena_empleado == (f'\nHola! soy un Empleado...'
                                  f'\n🆔 Identificacion es: {empleado.id}'
                                  f'\n👤 Nombre: {empleado.nombre} {empleado.apellido}'
                                  f'\n📅 Fecha de ingreso: {empleado.fecha_ingreso}'
                                  f'\n💼 Cargo: {empleado.cargo}'
                                  f'\n💰 Sueldo Mensual: ${empleado.sueldo}')

