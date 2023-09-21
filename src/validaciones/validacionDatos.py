def validar_nombre(nombre):
    try:
        # Verifica si el nombre contiene solo letras (sin espacios)
        if nombre.isalpha():
            return nombre
        else:
            raise ValueError("El nombre debe contener solo letras")
        
    except ValueError:
        print("\n¡Inténtelo nuevamente! - El nombre debe contener solo letras\n")
        nombre = input("Ingrese un nombre válido: ")
        return validar_nombre(nombre)

def validar_apellido(apellido):
    try:
        # Verifica si el apellido contiene solo letras (sin espacios)
        if apellido.isalpha():
            return apellido
        else:
            raise ValueError("El apellido debe contener solo letras")
        
    except ValueError:
        print("\n¡Inténtelo nuevamente! - El apellido debe contener solo letras\n")
        apellido = input("Ingrese un apellido válido: ")
        return validar_apellido(apellido)

def validar_identificacion(identificacion):
    try:
        # Verifica si la identificación es una cadena de exactamente 6 dígitos
        if identificacion.isdigit() and len(identificacion) == 6:
            return identificacion
        else:
            raise ValueError("La identificación debe ser una cadena de 6 dígitos")
            
    except ValueError:
        print("\n¡Inténtelo nuevamente! - La identificación debe ser una cadena de 6 dígitos\n")
        identificacion = input("Ingrese id válida (6 dígitos): ")
        return validar_identificacion(identificacion)
