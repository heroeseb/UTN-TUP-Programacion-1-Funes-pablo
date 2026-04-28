# 1) Dado el siguiente código, hacer una lista con los distintos errores que contiene y detallar qué
# tipo de error es cada uno.

'''a = 10
b = input("Introduce un número: ")
result = a / b'''  # TypeError: porque intentamos dividir un Integer con un String
# En el caso de que el input "b" se convirtiera a int, podría estar el potencial problema de un error ZeroDivisionError,
# porque el usuario podría ingresar un cero

'''print(f"Resultado: {result}")
numbers = [1, 2, 3]
print(numbers[5])'''  # IndexError: porque se intenta acceder a una posición del índice que no existe


# 2) Utilizando el código del ejercicio 1, arreglar los errores para que la ejecución del programa
# sea correcta sin necesidad de usar excepciones.

a = 10
b = input('Introduce un número: ').strip()
while not (b.isdigit() and b != '0'):
    print('¡Ingrese un número correcto!')
    b = input('Introduce un número: ').strip()

b = int(b)
result = a / b
print(f"Resultado: {result}")

numbers = [1, 2, 3]
print(numbers[2])


# 3) Utilizando el código del ejercicio 1, mantener el código con los errores originales e incluir
# bloques try-except para que la ejecución del programa no se frene al encontrar los errores.

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b
    print(f"Resultado: {result}")
    numbers = [1, 2, 3]
    print(numbers[5])
except:
    print('Error')

# 4) Repetir el ejercicio 3, pero usando excepciones múltiples que hagan alusión a los tipos de errores detectados.

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b
    print(f"Resultado: {result}")
except TypeError:
    print('Tipo de dato incorrecto')

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print('Número de índice inexistente')

# En este caso no usamos ZeroDivisionError porque input al devolver un string no va a pasar de TypeError

# 5) Repetir el ejercicio 4, pero esta vez incluyendo bloques else y finally.

try:
    a = 10
    b = int(input("Introduce un número: "))  # Lo casteo a int para que de esta forma pueda funcionar
    result = a / b
except TypeError:
    print('Tipo de dato incorrecto')
except ZeroDivisionError:
    print('No se puede dividir por cero')
else:
    print(f"Resultado: {result}")
finally:
    print('Fin de la división')

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print('Número de índice inexistente')
finally:
    print('Fin del ejercicio 5')

# 6) Escribir un programa que pida al usuario un número, y:
# ● Si el valor ingresado es válido, lo imprima por pantalla.
# ● Si el valor ingresado no es numérico, imprima por pantalla “Debe ingresar un número válido”.
# ● Si contiene algún otro tipo de error, imprima por pantalla “Se produjo un error inesperado” junto con el error que surgió.

try:
    numero = int(input('Dime un número entero: ').strip())
except ValueError:
    print('Debe ingresar un número válido')
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
else:
    print(f'Número ingresado: {numero}')

# 7) Repetir el ejercicio 6, pero añadiendo la posibilidad de que el usuario intente ingresar un nuevo número luego de encontrar un error.

while True:
    try:
        numero = int(input('Dime un número entero (mayor a cero): '))
        if numero <= 0:
            raise ValueError
    except ValueError:
        print('Debe ingresar un número válido')
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    else:
        print(f'Número ingresado: {numero}')
        break