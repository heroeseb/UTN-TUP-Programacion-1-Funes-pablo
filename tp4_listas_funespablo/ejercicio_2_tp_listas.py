
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