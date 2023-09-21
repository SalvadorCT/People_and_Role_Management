# Generar csv
import csv
import os

"""
Los archivos csv se crearan en la carpeta assets/datos cuando termine de ejecutar el programa
"""


# El os.getcwd() es para obtener la ruta absoluta de la carpeta donde se esta ejecutando el programa

# Convertir a csv
def persona_a_csv(lista):
    if len(lista) == 0:
        print('No hay personas registradas')
        return 0

    # Abre el archivo en modo escritura
    with open(f'{os.getcwd()}\\assets\\datos\\personas.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ID', 'Nombre', 'Apellido'])
        for persona in lista:
            writer.writerow([persona.id, persona.nombre, persona.apellido])
        file.flush()


def cliente_a_csv(lista):
    if len(lista) == 0:
        print('No hay clientes registradas')
        return 0
    with open(f'{os.getcwd()}\\assets\\datos\\clientes.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ID', 'Nombre', 'Apellido', 'Direccion Fiscal', 'Codigo Postal', 'Estado'])
        for cliente in lista:
            writer.writerow([cliente.id,
                             cliente.nombre,
                             cliente.apellido,
                             cliente.direccion_fiscal,
                             cliente.codigo_postal,
                             cliente.estado])
        file.flush()


def empleado_a_csv(lista):
    if len(lista) == 0:
        print('No hay empleados registradas')
        return 0
    with open(f'{os.getcwd()}\\assets\\datos\\empleados.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ID', 'Nombre', 'Apellido', 'Fecha Ingreso', 'Cargo', 'Sueldo'])
        for empleado in lista:
            writer.writerow([empleado.id,
                             empleado.nombre,
                             empleado.apellido,
                             empleado.fecha_ingreso,
                             empleado.cargo,
                             empleado.sueldo])
        file.flush()


def estudiante_a_csv(lista):
    if len(lista) == 0:
        print('No hay estudiantes registrados')
        return 0
    with open(f'{os.getcwd()}\\assets\\datos\\estudiantes.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ID', 'Nombre', 'Apellido', 'Semestre Matricula'])
        for estudiante in lista:
            writer.writerow([estudiante.id,
                             estudiante.nombre,
                             estudiante.apellido,
                             estudiante.semestre_matricula])
        file.flush()


# Leer csv
def leer_csv(archivo):
    try:
        with open(f'{os.getcwd()}\\assets\\datos\\{archivo}.csv', newline='') as File:
            reader = csv.reader(File, delimiter=';')
            print(f'Datos del archivo {archivo}.csv')
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f'El archivo {archivo}.csv no existe')

# import json
#
#
# def convertir_a_json(lista):
#     with open('personas.json', 'w') as file:
#         json.dump(lista, file, indent=4, sort_keys=True)
