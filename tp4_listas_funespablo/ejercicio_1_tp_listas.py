# Ejercicio 1 Nota de alumnos
lista_notas = [10,6,4,9,8,3,10,8,7,9]
num_alumno = 1
suma = 0
nota_alta = lista_notas[0]
nota_baja = lista_notas[0]
for i in lista_notas:
    print(f"Nota de alumno {num_alumno} : {i}")
    num_alumno += 1
    suma += i
    if i < nota_baja:
        nota_baja = i
    if i > nota_alta:
        nota_alta = i
promedio = suma/len(lista_notas)
print(f"El promedio es: {promedio}")
print(f"La nota más alta es: {nota_alta}")
print(f"La nota más baja es: {nota_baja}")