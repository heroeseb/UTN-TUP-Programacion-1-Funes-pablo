class EdadInvalidaError(Exception):
    pass

def registrar_edad(edad):
    if edad < 0 or edad > 120:
        raise EdadInvalidaError("La edad debe estar entre 0 y 120.")
    return edad

try:
    registrar_edad(-5)
except EdadInvalidaError as e:
    print(f"Error de validación: {e}")
except ValueError:
    print("Por favor, introduce un número entero.")



class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad < 0 or edad > 120:
        raise EdadInvalidaError("Edad fuera de rango (0-120).")
    return edad

while True:
    try:
        entrada = int(input("Introduce tu edad: "))
        edad = validar_edad(entrada)
        print(f"Edad registrada correctamente: {edad}")
        break
    except EdadInvalidaError as e:
        print(f"Error de validación: {e}")
    except ValueError:
        print("Por favor, introduce un número entero válido.")


class PrecioInvalidoError(Exception):
    pass

def validar_precio(precio):
    if(precio < 0 or precio > 10000):
        raise PrecioInvalidoError('El precio debe ser positivo y menor que $10000')
    return precio

while True:
    try:
        precio_us = float(input('Ingrese el precio: '))
        validar_precio(precio_us)
        print(f'El precio es {precio_us}')
        break
    except ValueError:
        print('Ingrese un número.')
    except PrecioInvalidoError as e:
        print(e)


class EdadMenorError(Exception):
    pass
class EdadMayorError(Exception):
    pass
def validar_edad(edad):
    if(edad < 0):
        raise EdadMenorError('La edad no puede ser menor a cero.')
    elif(edad > 120):
        raise EdadMayorError('La edad no puede ser mayor a 120.')
    return edad

# Programa principal
while True:
    try:
        edad_us = int(input('Ingrese su edad: '))
        validar_edad(edad_us)
        print(f'Su edad es {edad_us}')
        print(f'Usted nació en el año {2026 - edad_us}')
        break
    except ValueError:
        print('Debe ingresar un número entero.')
    except EdadMenorError as e:
        print(e)
    except EdadMayorError as e:
        print(e)