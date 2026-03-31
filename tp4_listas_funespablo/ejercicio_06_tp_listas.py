
# Ejercicio 6 Rotar hacia la derecha
numeros = [3, 7, 12, 25, 41, 56, 89]
print("La lista de números es: ")
for num in numeros:
    print(num,end=" ")
nueva_numeros = [0]
for i in range(len(numeros)):
    if i == 0:
        nueva_numeros[0] = numeros[-1]
    else:
        nueva_numeros.append(numeros[i-1])
print("\nLa lista con una posición adelante es: ")
for nuevos in nueva_numeros:
    print(nuevos,end=" ")