
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
