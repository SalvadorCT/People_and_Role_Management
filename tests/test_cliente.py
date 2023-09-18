from src.personas.cliente import Cliente
import pytest
def test_cliente():
    cliente = Cliente('12345678', 'Juan', 'Perez', ' 1234', +51, "soltero")
    assert cliente.id == '12345678'
    assert cliente.nombre == 'Juan'
    assert cliente.apellido == 'Perez'
    assert cliente.direccion_fiscal == ' 1234'
    assert cliente.codigo_postal == +51
    assert cliente.estado == "soltero"

