estudiantes = {
    "Ana": [7, 8, 9],
    "Luis": [6, 7, 5],
    "Marta": [10, 9, 9],
    "Roberto": [10, 10, 10]
}
promedio_list = []
for k,v in estudiantes.items():
    sumaa = 0
    for nota in v:
        sumaa += nota
    promedio = sumaa / len(v)
    promedio_list.append((k,promedio))

def ordenar_tupla(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][1] < lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

ordenar_tupla(promedio_list)

print("El promedio de cada estudiante es: ")
for i in range(len(promedio_list)):
    print(f"Estudiante: {promedio_list[i][0]}, Promedio: {promedio_list[i][1]:.2f}")

print(f"El estudiante con mejor promedio es: {promedio_list[0][0]} con promedio de {promedio_list[0][1]}")

def aprobados(lista):
    resultado = []
    for alumno,promedio in lista:
        if promedio >= 6:
            resultado.append((alumno,promedio))
    return resultado
print(f"Los estudiantes aprobados son: ")
for alum,prom in aprobados(promedio_list):
    print(f"{alum}: {prom:.2f}")