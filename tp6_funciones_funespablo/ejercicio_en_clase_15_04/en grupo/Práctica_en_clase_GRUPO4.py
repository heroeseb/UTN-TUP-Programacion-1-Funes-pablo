from Funciones_en_clase_GRUPO4 import *
import random
    #Ejercicio 1
notas=[]
while len(notas)<10:
    nota=input("Ingrese una nota (Del 1 al 10): ")
    while not nota.isdigit() or not (0 < int(nota) <= 10):
        print("Valor incorrecto... Intente nuevamente!")
        nota=input("Ingrese una nota (Del 1 al 10): ")
    notas.append(int(nota))
    print("Nota ingresada correctamente!")
print(f"La lista de notas es: {", ".join(map(str, notas))}")
print(f"El promedio de todas las notas es de: {calcular_promedio(notas)}")
print("-"*50)

    # Ejercicio 2
aprobados = filtrar_aprobados(notas)
print(f"Notas aprobadas: {", ".join(map(str, aprobados))}")
print(f"Cantidad de aprobados: {len(aprobados)}")
print(f"Porcentaje de aprobados: {len(aprobados) / len(notas) * 100:.2f}%")
print("-"*50)

    # Ejercicio 3
analizar_notas(notas)