from Funciones.ejercicio_13_05 import *

print('Ejercicio 1')
numeros = []

for i in range(5):
    while True:
        try:
            numero = float(input(f'Ingrese el numero {i+1}: '))
            numeros.append(numeros)
            break
        except ValueError:
            print('Debe ingresar un numero!')

promedio = calcular_promedio(numeros)

if promedio != 0:
    print(f'El promedio de los numeros ingresados es: {promedio:.2f}')

print(f'El max es: {max(numeros)}')
print(f'El min es: {min(numeros)}')

# Definición de la función necesaria (esto iría en Funciones.funciones_4)
def convertir_a_set(lista):
    return set(lista)

# --- Código de la imagen image_dbcbda.png ---

print('Ejercicio 4')

alumnos = ["Ana", "Luis", "Ana", "Pedro", "Luis", "Carla"]

set_alumnos = convertir_a_set(alumnos)
print(f'Los alumnos sin repetir son: {set_alumnos}')
print(f'La cantidad de alumnos unicos es {len(set_alumnos)}')

set_ordenado = sorted(set_alumnos)
print(f'Alumnos ordenados alfabeticamente: {set_ordenado}')

lista_alumnos = list(set_alumnos)
print(lista_alumnos)