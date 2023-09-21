from personas.persona import Persona
from personas.cliente import Cliente
from personas.estudiante import Estudiante
from personas.empleado import Empleado
from assets.generar_cvs import *
from validaciones.validacionDatos import *


def menu_pricinpal():
    print('''1. Crear Persona
2. Crear Estudiante
3. Crear Cliente
4. Crear Empleado
5. Mostrar informacion
6. Generar CSV
7. Leer CSV
8. Salir
    ''')
    opcion = input('Ingrese una opcion: ')
    return opcion


# def menu_persona():
#     print('''
#     1. Crear Persona
#     2. Generar CSV
#     3. Salir
#     ''')
#     opcion = input('Ingrese una opcion: ')
#     return opcion
#
#
# def menu_estudiante():
#     print('''
#     1. Crear Estudiante
#     2. Generar CSV
#     3. Salir
#     ''')
#     opcion = input('Ingrese una opcion: ')
#     return opcion
#
#
# def menu_cliente():
#     print('''
#     1. Crear Cliente
#     2. Generar CSV
#     3. Salir
#     ''')
#     opcion = input('Ingrese una opcion: ')
#     return opcion
#
#
# def menu_empleado():
#     print('''
#     1. Crear Empleado
#     2. Generar CSV
#     3. Salir
#     ''')
#     opcion = input('Ingrese una opcion: ')
#     return opcion


def crear_persona():
    id = validar_numero_largo("Ingrese la Identificacion: ", 6)
    nombre = validar_texto('Ingrese el Nombre: ')
    apellido = validar_texto('Ingrese el Apellido: ')
    persona = Persona(id, nombre, apellido)
    return persona


def crear_estudiante():
    id = validar_numero_largo("Ingrese la Identificacion: ", 6)
    nombre = validar_texto('Ingrese el Nombre: ')
    apellido = validar_texto('Ingrese el Apellido: ')
    semestre = verificar_numero_rango('Ingrese el Semestre de Matricula: ', 1, 10)
    estudiante = Estudiante(id, nombre, apellido, semestre)
    return estudiante


def crear_cliente():
    id = validar_numero_largo("Ingrese la Identificacion: ", 6)
    nombre = validar_texto('Ingrese el Nombre: ')
    apellido = validar_texto('Ingrese el Apellido: ')
    direccion = validar_texto('Ingrese la Direccion Fiscal: ')
    codigo = validar_numero_largo('Ingrese el Codigo Postal: ', 10)
    estado = validar_texto('Ingrese el Estado: ')
    cliente = Cliente(id, nombre, apellido, direccion, codigo, estado)
    return cliente


def crear_empleado():
    id = validar_numero_largo("Ingrese la Identificacion: ", 6)
    nombre = validar_texto('Ingrese el Nombre: ')
    apellido = validar_texto('Ingrese el Apellido: ')
    fecha = input('Ingrese la Fecha de Ingreso: ')
    cargo = validar_texto('Ingrese el Cargo: ')
    sueldo = verificar_numero_rango('Ingrese el Sueldo: ', 1, 100000)
    empleado = Empleado(id, nombre, apellido, fecha, cargo, sueldo)
    return empleado


def crear_cvs(personas, estudiantes, clientes, empleados):
    persona_a_csv(personas)
    estudiante_a_csv(estudiantes)
    cliente_a_csv(clientes)
    empleado_a_csv(empleados)


def imprimir_csv():
    leer_csv("personas")
    leer_csv("estudiantes")
    leer_csv("clientes")
    leer_csv("empleados")


def imprimir(objetos, nombre):
    if not objetos:
        print(f'No hay informacion de {nombre}')
        return None
    for objeto in objetos:
        print(objeto)
        objeto.adicional_info()
