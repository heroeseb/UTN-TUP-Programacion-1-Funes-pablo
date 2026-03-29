
# Ejercicio 2 Lista ordenada con opción de eliminar
lista_productos = []
for i in range(5):
    while True:
        producto = input("Dime un producto: ").strip()
        if producto.replace(" ","").isalpha():
            lista_productos.append(producto)
            break
        else:
            print("Por favor, ingrese un nombre válido. No se permiten números, solo letras....")
lista_ordenada = sorted(lista_productos)
print("La lista ordenada es: ")
for product in lista_ordenada:
    print(f"- {product}")
while True:
    eliminar = input("Dime qué producto quieres eliminar (ingrese 0 para terminar): ")
    if eliminar == "0":
        print("La lista de producto sin el artículo eliminado es: ")
        break
    if eliminar in lista_ordenada:
        lista_ordenada.remove(eliminar)
    else:
        print("Ingrese un producto que esté en la lista para poder eliminarlo...")
for product in lista_ordenada:
    print(f"- {product}")
# Ejercicio 3 Lista pares e impares
lista = []
pares = []
impares = []
import random
for i in range(15):
    numero = random.randint(1,100)
    lista.append(numero)
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Los números de la lista ({len(lista)} números) son: ")
for num in lista:
    print(num,end=" ")
print(f"\nLos números pares son {len(pares)}: ")
for num in pares:
    print(num,end=" ")
print(f"\nLos números impares son {len(impares)}: ")
for num in impares:
    print(num,end=" ")
# Ejercicio 4 Valores repetidos
datos = [1,3,5,3,7,1,9,5,3]
print("La lista completa es: ")
for dato in datos:
    print(dato,end=" ")
lista_nueva = []
for dat in datos:
    if dat in lista_nueva:
        continue
    else:
        lista_nueva.append(dat)
print(f"\nLa lista sin repetir números es: ")
for numero_nuevo in lista_nueva:
    print(numero_nuevo,end=" ")
# Ejercicio 5 Agregar o quitar en una lista
alumnos = ["Laura","Diego","Lucas","Paula","Bruno","Sofia","Carla","Tomas"]
print("Los alumnos presentes son: ")
for alumno in alumnos:
    print(alumno,end=" ")
while True:
    opcion = input("Dime si quieres agregar un nuevo estudiante (1) o eliminar uno ya existente en la lista (2) o si quieres salir del menú (0): ")
    if opcion == "0":
        break
    elif opcion == "1":
        agregar = input("Dime el nombre del alumno que quieres agregar: ")
        alumnos.append(agregar)
    elif opcion == "2":
        while True:
            quitar = input("Dime el nombre del alumno que quieres quitar: ")
            if quitar in alumnos:
                alumnos.remove(quitar)
                break
            else:
                print("Dime un nombre de alumno correcto...")
    else:
        print("Ingresa una opción válida con el número 1 o 2...")
print("La lista de alumnos actualizada es: ")
for alumno in alumnos:
    print(alumno,end=" ")
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
# Ejercicio 7 Matriz temperatura Min y Max
temperaturas = [
    [11, 25],  # Lunes
    [13, 20],  # Martes
    [11, 21],  # Miércoles
    [13, 23],  # Jueves
    [16, 27],  # Viernes
    [16, 26],  # Sábado
    [8, 15]   # Domingo
]
sum_min = 0
sum_max = 0
mayor_amplitud = 0
mayor_amplitud_dia = 0
contador = 0
for minimo,maximo in temperaturas:
    print(f"Min {minimo}° - Max {maximo}°")
    contador += 1
    sum_max += maximo
    sum_min += minimo
    amplitud = maximo - minimo
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        mayor_amplitud_dia = contador
print(f"El promedio de las temperaturas máximas es: {(sum_max/7):.0f}°")
print(f"El promedio de las temperaturas mínimas es: {(sum_min/7):.0f}°")
print(f"El día que se registró la mayor amplitud térmica fue: Min {temperaturas[mayor_amplitud_dia-1][0]} ° - Max {temperaturas[mayor_amplitud_dia-1][1]}°")
# Ejercicio 8 Notas de estudiantes
notas = [
    ["Ana", 8.5, 7.0, 9.0],
    ["Luis", 6.0, 8.0, 7.5],
    ["María", 9.0, 9.5, 8.0],
    ["Carlos", 7.0, 6.5, 8.5],
    ["Sofía", 8.0, 7.5, 9.0]
]
suma_materi1 = 0
suma_materi2 = 0
suma_materi3 = 0
for nombre, nota1, nota2, nota3 in notas:
    promedio = (nota1 + nota2 + nota3) / 3
    suma_materi1 += nota1
    suma_materi2 += nota2
    suma_materi3 += nota3
    print(f"{nombre} : materia 1 : {nota1}, materia 2 : {nota2}, materia 3 : {nota3} , su promedio de notas es: {promedio:.2f}")
print(f"""El promedio de las materias son: 
    materia 1 : {suma_materi1/len(notas):.2f}
    materia 2 : {suma_materi2/len(notas):.2f} 
    materia 3 : {suma_materi3/len(notas):.2f}
    """)
# Ejercicio 9 Ta-te-ti
tablero = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]
contador = 0
while True:
    if (tablero[0][0] == tablero[0][1] == tablero[0][2] != "-") or (tablero[1][0] == tablero[1][1] == tablero[1][2] != "-") or (tablero[2][0] == tablero[2][1] == tablero[2][2] != "-") or (tablero[0][0] == tablero[1][0] == tablero[2][0] != "-") or (tablero[0][1] == tablero[1][1] == tablero[2][1] != "-") or (tablero[0][2] == tablero[1][2] == tablero[2][2] != "-") or (tablero[0][0] == tablero[1][1] == tablero[2][2] != "-") or (tablero[0][2] == tablero[1][1] == tablero[2][0] != "-"):
        print("Hay un ganador, ha terminado el juego")
        break
    if contador == 9:
        print("Empate, se terminó el juego")
        break
    if contador%2 == 0:
        jugador1 = int(input("""Ingrese el movimiento del jugador 1 con un número (usa 0 para terminar el juego): 
                        |1,2,3|
                        |4,5,6|
                        |7,8,9|"""))
        match jugador1:
            case 0:
                print("Ha terminado el juego, resultado del tablero: ")
                for i in tablero:
                    print("|",end="")
                    for j in i:
                        print(j,end="|")
                    print("")
                break
            case 1:
                if tablero[0][0] == "-":
                    tablero[0][0] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 2:
                if tablero[0][1] == "-":
                    tablero[0][1] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 3:
                if tablero[0][2] == "-":
                    tablero[0][2] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 4:
                if tablero[1][0] == "-":
                    tablero[1][0] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 5:
                if tablero[1][1] == "-":
                    tablero[1][1] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 6:
                if tablero[1][2] == "-":
                    tablero[1][2] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 7:
                if tablero[2][0] == "-":
                    tablero[2][0] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 8:
                if tablero[2][1] == "-":
                    tablero[2][1] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 9:
                if tablero[2][2] == "-":
                    tablero[2][2] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
        print("Tablero: ")
        for i in tablero:
            print("|",end="")
            for j in i:
                print(j,end="|")
            print("")
        contador += 1
    else:
        jugador2 = int(input("""Ingrese el movimiento del jugador 2 con un número (usa 0 para terminar el juego): 
                        |1,2,3|
                        |4,5,6|
                        |7,8,9|"""))
        match jugador2:
            case 0:
                print("Ha terminado el juego, resultado del tablero: ")
                for i in tablero:
                    print("|",end="")
                    for j in i:
                        print(j,end="|")
                    print("")
                break
            case 1:
                if tablero[0][0] == "-":
                    tablero[0][0] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 2:
                if tablero[0][1] == "-":
                    tablero[0][1] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 3:
                if tablero[0][2] == "-":
                    tablero[0][2] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 4:
                if tablero[1][0] == "-":
                    tablero[1][0] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 5:
                if tablero[1][1] == "-":
                    tablero[1][1] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 6:
                if tablero[1][2] == "-":
                    tablero[1][2] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 7:
                if tablero[2][0] == "-":
                    tablero[2][0] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 8:
                if tablero[2][1] == "-":
                    tablero[2][1] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 9:
                if tablero[2][2] == "-":
                    tablero[2][2] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
        print("Tablero: ")
        for i in tablero:
            print("|",end="")
            for j in i:
                print(j,end="|")
            print("")
        contador += 1
# Ejercicio 10 Registro de ventas en matriz 4x7
ventas = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
total1 = 0
total2 = 0
total3 = 0
total4 = 0
mayores_ventas = 0
dia_mayores_ventas = 0
for i in range(len(ventas)):
    print(f"\nDía {i + 1}")
    producto1 = int(input("Dime la cantidad vendida del producto 1: "))
    producto2 = int(input("Dime la cantidad vendida del producto 2: "))
    producto3 = int(input("Dime la cantidad vendida del producto 3: "))
    producto4 = int(input("Dime la cantidad vendida del producto 4: "))
    ventas[i] = [producto1, producto2, producto3, producto4]
    total1 += producto1
    total2 += producto2
    total3 += producto3
    total4 += producto4
    total_dia = producto1 + producto2 + producto3 + producto4
    if total_dia > mayores_ventas:
        mayores_ventas = total_dia
        dia_mayores_ventas = i
print("\nPRODUCTO MÁS VENDIDO POR DÍA")
for i in range(len(ventas)):
    vendido_dia = ventas[i][0]
    indice_vendido = 0
    for j in range(1, len(ventas[i])):
        if ventas[i][j] > vendido_dia:
            vendido_dia = ventas[i][j]
            indice_vendido = j
    print(
        f"El producto más vendido del día {i + 1} "
        f"es el producto {indice_vendido + 1} "
        f"con {vendido_dia} unidades vendidas"
    )
print(f"""
TOTALES SEMANALES
El total de producto 1 vendido los {len(ventas)} días es: {total1}
El total de producto 2 vendido los {len(ventas)} días es: {total2}
El total de producto 3 vendido los {len(ventas)} días es: {total3}
El total de producto 4 vendido los {len(ventas)} días es: {total4}
""")
print(f"El día de mayores ventas fue el día {dia_mayores_ventas + 1}")
print("Ventas de ese día:")
for i, cantidad in enumerate(ventas[dia_mayores_ventas]):
    print(f"Producto {i + 1}: {cantidad}", end=" ")
print(f"\nCon un total de {mayores_ventas} unidades vendidas")
if total1 >= total2 and total1 >= total3 and total1 >= total4:
    producto = 1
    total = total1
elif total2 >= total1 and total2 >= total3 and total2 >= total4:
    producto = 2
    total = total2
elif total3 >= total1 and total3 >= total2 and total3 >= total4:
    producto = 3
    total = total3
else:
    producto = 4
    total = total4
print(
    f"\nEl producto más vendido de la semana es el producto {producto} "
    f"con un total de {total} unidades vendidas"
)
