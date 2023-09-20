# Gestión de Personas y Roles

---

## Contenido

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Estructura del programa](#estructura-del-programa)
3. [Instrucciones de Uso](#instrucciones-de-uso)
4. [Installation](#instalacion)
5. [Dependencias](#dependencias)
6. [Licencia](#licencia)
7. [Contribuciones](#contribuciones)
## Descripción del Proyecto

- Este proyecto de gestión de personas y roles permite realizar un seguimiento de estudiantes, clientes y empleados. 
- Puedes agregar, listar y guardar los datos en un archivo CSV.

## Estructura del programa
```
People_and_Role_Management
├── docs/
│   └── user_guide.md
│   
├── src/
|   ├── assets/
│   |   ├── __init__.py
│   │   └── generar_cvs.py
|   |
│   ├── personas/
│   │   ├── __init__.py
│   │   ├── cliente.py
│   │   ├── empleado.py
│   │   ├── estudiante.py
│   │   └── persona.py
|   |
│   ├── __init__.py
│   ├── main.py
│   └── menu.py
|
├── test/
|   ├── __init__.py
|   ├── test_cliente.py
│   ├── test_empleado.py
│   ├── test_estudiante.py
│   └── test_persona.py
|
├── .gitignore
├── LICENSE
└── README.md
```
## Instrucciones de Uso

1. Clona este repositorio en tu máquina local.
2. Ejecuta `main.py` para iniciar el programa.
3. Sigue las instrucciones en pantalla para gestionar personas y roles.

## Instalacion

* Introduccion para la instalacion

- Clone the repository
```
git clone  <git lab template url> <project_name>
```
- Ingresar a la Carpeta o  Ruta donde se encuentra
```
cd ../path/to/the/file
```

## Dependencias

Este proyecto utiliza Python 3 y no requiere la instalación de bibliotecas adicionales.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir o informar de problemas, crea un problema o envía una solicitud de extracción en el repositorio.