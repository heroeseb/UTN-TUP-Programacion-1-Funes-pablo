from funciones_personal import *
# creamos la lista
lista_numeros = input_lista_intfloat("Dime la nota(numeros menor a 10): ",10,10)
# Ejercicio 1: Promedio de notas
print(f"El promedio es {calcular_promedio(lista_numeros):.2f}")
# Ejercicio 2: Filtrar y contar aprobados
aprobados = filtrar_aprobados(lista_numeros,6)
print("Los aprobados son:")
print(*aprobados,sep=",")
print(f"La cantidad de aprobados son {len(aprobados)}")
print(f"El porcentaje de aprobados es: %{len(aprobados)*100/len(lista_numeros)}")
# Ejercicio 3: Análisis completo de notas
prom,maxi,mini = analizar_notas(lista_numeros)
print(f'''
    El analisis de notas completo es:
    -promedio: {prom}
    -nota mas alta: {maxi}
    -nota mas baja: {mini}
    ''')
