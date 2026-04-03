# Grupo 7
nombres_prod = []
stock_prod = []
precios_prod = []

while True:
    print("""
        1. Alta Individual.
        2. Carga Masiva.
        3. Baja de Producto.
        4. Consultas Rápidas: Buscar un producto por nombre y elegir si ver su Stock o su Precio.
        5. Movimientos de Stock:
        - Vender: Restar una cantidad al stock
        - Reponer: Sumar una cantidad al stock existente.
        6. Alerta de Agotados.
        7. Listado General.
        8. Salir.
        """)
    opcion = input("Ingrese una opción: ")
    match opcion:
        case "1":
            producto = input("Dime el nombre del producto: ").strip()
            stock = input("Ingrese el stock del producto: ").strip()
            precio = input("Ingrese el precio: ").strip()
            if producto.replace(" ","").isalpha() and  stock.isdigit() and precio.isdigit():
                nombres_prod.append(producto.capitalize())
                stock_prod.append(int(stock))
                precios_prod.append(int(precio))
            else:
                print("Error datos incorrectos...")
        case "2":
            cantidad = input("Dime la cantidad de productos a ingresar: ")
            if cantidad.isdigit() and int(cantidad) > 0:
                for i in range(int(cantidad)):
                    while True:
                        producto = input("Dime el nombre del producto: ").strip()
                        stock = input("Ingrese el stock del producto: ").strip()
                        precio = input("Ingrese el precio: ").strip()
                        if producto.replace(" ","").isalpha() and  stock.isdigit() and precio.isdigit():
                            nombres_prod.append(producto.capitalize())
                            stock_prod.append(int(stock))
                            precios_prod.append(int(precio))
                            break
                        else:
                            print("Error datos incorrectos...")
            else:
                print("Error tiene que ingresar un numero validdo")
        case "3":
            baja_prod = input("Ingrese el nobmre del producto a eliminar: ").strip()
            if baja_prod.replace(" ","").isalpha() and baja_prod.capitalize() in nombres_prod:
                posicion_prod = nombres_prod.index(baja_prod.capitalize())
                nombres_prod.remove(posicion_prod)
                precios_prod.remove(posicion_prod)
                stock_prod.remove(posicion_prod)
                print(f"Producto eliminado {baja_prod.capitalize()}!!")
            else:
                print(f"El producto {baja_prod.capitalize()} no se encuentra en el stock o escribio mal el nombre...")
        case "4":
            while True:
                nombre = input("Ingrese el nombre del producto: ").strip()
                if nombre.replace(" ","").isalpha() and nombre.capitalize() in nombres_prod:
                    print("""
                        1- Ver stock del producto
                        2- Ver precio del producto
                        3- Salir
                        """)
                    opcion = input("Ingrese una opción: ").strip()
                    match opcion:
                        case "1":
                            numero_index = nombres_prod.index(nombre.capitalize())
                            print(f"El stock del producto {nombre.capitalize()} es {stock_prod[numero_index]}")
                        case "2":
                            numero_index = nombres_prod.index(nombre.capitalize())
                            print(f"El precio del producto {nombre.capitalize()} es {precios_prod[numero_index]}")
                        case "3":
                            print("Saliendo de la consulta...")
                            break
                        case _:
                            print("Error escriba una opcion correcta...")
                    break
                else:
                    print("Ingrese una opción valida...")
        case "5":
            while True:
                nombre = input("Ingrese el nombre del producto: ").strip()
                if nombre.replace(" ","").isalpha() and nombre.capitalize() in nombres_prod:
                    numero_index = nombres_prod.index(nombre.capitalize())
                    print("""
                        1- Vender producto
                        2- Reponer stock
                        3- Salir
                        """)
                    opcion = input("Ingrese una opción: ").strip()
                    match opcion:
                        case "1":
                            cant_vender = input("Ingrese la cantidad que desea vender: ").strip()
                            if cant_vender.isdigit() and int(cant_vender) > 0 and int(cant_vender) <= stock_prod[numero_index]:
                                stock_prod[numero_index] -= int(cant_vender)
                                print(f"Usted vendio correctamente el producto {nombre.capitalize()}")
                                print(f"El stock actual del producto {nombre.capitalize()} es {stock_prod[numero_index]}")
                            else:
                                print("Quiere vender mas producto de lo que hay en existencia..")
                        case "2":
                            cant_sumar = input("Ingrese la cantidad que desea reponer: ").strip()
                            if cant_sumar.isdigit() and int(cant_sumar) > 0 and int(cant_sumar) <= stock_prod[numero_index]:
                                stock_prod[numero_index] += int(cant_sumar)
                                print(f"Usted agrego stock correctamente del producto {nombre.capitalize()}")
                                print(f"El stock actual del producto {nombre.capitalize()} es {stock_prod[numero_index]}")
                        case "3":
                            print("Saliendo de la consulta...")
                            break
                        case _:
                            print("Error escriba una opcion correcta...")
                    break
                else:
                    print("Ingrese una opción valida...")
        case "6":
            if stock_prod:
                if 0 in stock_prod:
                    for i in range(len(stock_prod)):
                        if stock_prod[i] == 0:
                            print(f"El producto {nombres_prod[i]} esta agotado")
                else:
                    print("No hay productos agotados")
            else:
                print("La lista aun no se inicializa...")
        case "7":
            print("Nombre del producto | Stock | Precio")
            for i in range(len(nombres_prod)):
                print(f"{nombres_prod[i]} | {stock_prod[i]} | ${precios_prod[i]}")
        case "8":
            print("Hasta luego!")
            break
        case _:
            print("Escribi bien flaco...")