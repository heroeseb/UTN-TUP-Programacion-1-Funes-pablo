from funciones.funciones_4 import *

print("Ejercicio 4")

alumnos = ["Ana", "Luis", "Ana", "Pedro", "Luis", "Carla"]

set_alumnos = convertir_a_set(alumnos)
print(f"Los alumnos sin repetir son: {", ".join(set_alumnos)}")
print(f"La cantidad de alumnos unicos es {len(set_alumnos)}")

set_ordenado = sorted(set_alumnos)
print(f"Alumnos ordenados alfabeticamente: {", ".join(set_ordenado)}")

lista_alumnos = list(set_alumnos)
print(", ".join(lista_alumnos))