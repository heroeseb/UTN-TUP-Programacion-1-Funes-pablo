# Ejercicio 1— “Caja del Kiosco”

total = 0
total_c_descuento = 0
ahorro = 0
while True:
    nombre_cliente = input("Introduce el nombre del cliente: ").strip()
    if nombre_cliente.replace(" ","").isalpha():
        break
    else:
        print("Ingrese un nombre correcto...")
while True:
    cantidad_productos = input("Introduce la cantidad de productos: ").strip()
    if cantidad_productos.isdigit():
        cant_convert_numero = int(cantidad_productos)
        if cant_convert_numero > 0:
            break
        else:
            print("El número tiene que ser mayor que 0")
    else:
        print("Ingrese un número correcto...")
print(f"Cliente : {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")
for i in range (cant_convert_numero):
    while True:
        precio = input("Precio del producto: ").strip()
        if precio.replace(".","").isdigit():
            precio_entero = float(precio)
            break
        else:
            print("Ingrese un número correcto...")
    while True:
        tiene_descuento = input("Tiene descuento (S,N)?: ").strip()
        if (tiene_descuento.lower() == "s") or (tiene_descuento.lower() == "n"):
            tiene_descuento_lower = tiene_descuento.lower()
            break
        else:
            print("Ingrese un dato correcto (s o n)...")
    if tiene_descuento_lower == "s":
        cantidad_descuento = precio_entero * 0.10
        ahorro += cantidad_descuento
        total_c_descuento += precio_entero - cantidad_descuento
    else:
        total_c_descuento += precio_entero
    total += precio_entero
    print(f"Producto {i+1} - Precio: {precio} Descuento (S/N): {tiene_descuento_lower}")
promedio = total_c_descuento / cant_convert_numero
print(f"Total sin descuentos: ${total}")
print(f"Total con descuentos: ${total_c_descuento}")
print(f"Ahorro: ${ahorro}")
print(f"Promedio por producto: ${promedio:.2f}")
