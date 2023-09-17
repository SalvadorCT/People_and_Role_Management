from personas.persona import Persona
from personas.cliente import Cliente
from personas.estudiante import Estudiante
from personas.empleado import Empleado

obj1 = Persona(12345678, 'Finn', 'Mertens')

obj2 = Estudiante(24681012, 'Dwayne', 'Johnson', 5)

obj3 = Cliente(4043243, 'Homero', 'J. Simpson', 'Avenida Siempre Viva 742', 49007, 'Springfield')

obj4 = Empleado(2000569, 'Larry', 'Needlemeyer', 2005, 'supervisor')

def imprimir(objeto):
    print(objeto)
    objeto.adicional_info()

imprimir(obj1)
imprimir(obj2)
imprimir(obj3)
imprimir(obj4)