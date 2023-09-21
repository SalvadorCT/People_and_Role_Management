def validar_texto(mensaje):
    nombre = input(mensaje)
    try:
        # Verifica si el nombre contiene solo letras incluyendo los espacios
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            raise ValueError("El texto debe contener solo letras")

    except ValueError:
        print(f"\n¡Inténtelo nuevamente! - El texto debe contener solo letras\n")
        return validar_texto(mensaje)


def validar_numero_largo(mensaje, large):
    identificacion = input(mensaje)
    try:
        # Verifica si la identificación es una cadena de exactamente 6 dígitos
        if identificacion.isdigit() and len(identificacion) == large:
            return int(identificacion)
        else:
            raise ValueError("Los digitos debe ser una cadena de 6 dígitos")

    except ValueError:
        print(f"\n¡Inténtelo nuevamente! - Los digitos debe ser una cadena de {large} dígitos\n")
        return validar_numero_largo(mensaje, large)


def verificar_numero_rango(mensaje, minimo, maximo):
    numero = input(mensaje)
    try:
        if numero.isdigit() and minimo <= int(numero) <= maximo:
            return int(numero)
        else:
            raise ValueError(f"El numero debe ser un entero entre {minimo} y {maximo}")

    except ValueError:
        print(f"\n¡Inténtelo nuevamente! - El numero debe ser un entero entre {minimo} y {maximo}\n")

        return verificar_numero_rango(mensaje, minimo, maximo)
