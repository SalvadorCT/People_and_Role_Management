from menu import *


def main():
    personas = []
    estudiantes = []
    clientes = []
    empleados = []
    while True:
        opcion = menu_pricinpal()
        if opcion == '1':
            persona = crear_persona()
            personas.append(persona)
            print("Persona creada con exito")

        elif opcion == '2':
            estudiante = crear_estudiante()
            estudiantes.append(estudiante)
            print("Estudiante creado con exito")

        elif opcion == '3':
            cliente = crear_cliente()
            clientes.append(cliente)
            print("Cliente creado con exito")

        elif opcion == '4':
            empleado = crear_empleado()
            empleados.append(empleado)
            print("Empleado creado con exito")

        elif opcion == '5':
            imprimir(personas, 'Personas')
            imprimir(estudiantes, 'Estudiantes')
            imprimir(clientes, 'Clientes')
            imprimir(empleados, 'Empleados')

        elif opcion == '6':
            crear_cvs(personas, estudiantes, clientes, empleados)

        elif opcion == '7':

            imprimir_csv()

        elif opcion == '8':
            print('Gracias por usar el programa')
            break
        else:
            print('Por favor ingrese una opcion valida')


if __name__ == '__main__':
    main()
