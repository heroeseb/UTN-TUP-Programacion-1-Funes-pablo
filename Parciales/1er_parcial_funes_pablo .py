# Alumno Funes Pablo Sebastian
herramientas = ["Martillo"]
existencias = [0]
while True:
  print("""
1. Carga Inicial de Herramientas
2. Carga de Existencias
3. Visualización de Inventario
4. Consulta de Stock
5. Reporte de Agotados
6. Alta de Nuevo Producto
7. Actualización de Stock (Venta/Ingreso):
8. Salir: Finalizar la ejecución del sistema.
        """)
  opcion = input("Ingrese la opción: ").strip()
  while not opcion.isdigit():
    print("Ingrese numero correcto de opcion")
    opcion = input("")
  if opcion == "1":
    cantidad = input ("Ingrese la cantidad de herramientas a ingesar: ").strip()
    while not (cantidad.isdigit() and cantidad != "0"):
      print("Ingrese un numero y que sea mayor a 0")
      cantidad = input("Ingrese la cantidad de herramientas a ingesar: ")
    for i in range(int(cantidad)):
      while True:
        herramienta_carga = input("Dime el nombre de la herramienta que deseas cargar: ")
        if herramienta_carga.isalpha() and (herramienta_carga.capitalize() not in herramientas):
          herramientas.append(herramienta_carga.capitalize())
          existencias.append(0)
          print(f"Herramienta {herramienta_carga.capitalize()} se cargo con exito!!")
          break
        else:
          print("La herramienta ya esta en la lista")
  elif opcion == "2":
    if herramientas and existencias:
      for i in range(len(existencias)):
        print(f"Ingrese las existencias del articulo {herramientas[i]} actualmente tiene {existencias[i]}")
        while True:
          cantidad_existencia_agegar = input("Ingrese cantidad: ").strip()
          if cantidad_existencia_agegar.isdigit():
            existencias[i] = int(cantidad_existencia_agegar)
            print(f"Se agrego correctamente la cantidad de {existencias[i]} a la herramienta {herramientas[i]}")
            break
          else:
            print("Ingrese un numero correcto...")
      else:
        print("Aun no se inicializo la lista")
  elif opcion == "3":
    if herramientas and existencias:
      print("Stock de herramientas:")
      for i in range(len(herramientas)):
        print(f"{herramientas[i]} : {existencias[i]} unidades.")
    else:
      print("Aun no se inicializo la lista..")
  elif opcion == "4":
    while True:
      nombre_herramienta = input("Ingrese el nomber de la herramienta que desea buscar su stock: ").strip()
      if nombre_herramienta.isalpha():
        if nombre_herramienta.capitalize() in herramientas:
          indice_herramienta = herramientas.index(nombre_herramienta.capitalize())
          print(f"La herramienta {herramientas[indice_herramienta]} tiene {existencias[indice_herramienta]} unidades en su stock.")
          break
        else:
          print(f"La herramienta {nombre_herramienta.capitalize()} no esta en la lista.")
      else:
        print("Ingrese nombre solo con letras...")
  elif opcion == "5":
    if herramientas and existencias:
      print("Productos con existencias agotadas: ")
      no_hay_agotado = True
      for i in range(len(existencias)):
        if existencias[i] <= 0:
          print(f"{herramientas[i]} : {existencias[i]}")
          no_hay_agotado = False
      if no_hay_agotado:
        print("No hay productos agotados.")
    else:
      print("La lista no ha sido inicializada")
  elif opcion == "6":
    producto_agegar = input("Dime el nombre del producto que deseas agegar: ").strip()
    if producto_agegar.isalpha() and (producto_agegar.capitalize() not in herramientas):
      agregar_existencia = input("Dime la cantidad de existencia a agregar: ").strip()
      if agregar_existencia.isdigit() and int(agregar_existencia) > 0:
        herramientas.append(producto_agegar.capitalize())
        existencias.append(int(agregar_existencia))
        print(f"Se agego {producto_agegar.capitalize()} correctamente con {int(agregar_existencia)} unidades en existencia!!")
      else:
        print("Ingrese un numero correcto")
    else:
      print("Ingrese una nombre correcto y que no este en la ista")
  elif opcion == "7":
    if herramientas and existencias:
      while True:
        print("""
              1. Ventas
              2. Ingresos
              """)
        opcion_voi = input("Ingrese opcion: ").strip()
        if opcion_voi.isdigit():
          if opcion_voi == "1":
            producto_vender = input("Ingrese el nombre del producto a vender: ").strip()
            if producto_vender.capitalize() in herramientas:
              indice = herramientas.index(producto_vender.capitalize())
              can_vender = input("Ingrese la cantidad a vender:").strip()
              if can_vender.isdigit() and int(can_vender) > 0 and (existencias[indice] >= int(can_vender)):
                existencias[indice] -= int(can_vender)
                print(f"Se resto {int(can_vender)} unidades del producto {herramientas[indice]}")
                print(f"Stock actual : {existencias[indice]}")
                break
              else:
                print("Error no hay existencia suficiente o la cantidad ingresada esta mal escrita(solo numeros)")
            else:
              print("El producto no esta en la lista")
          elif opcion_voi == "2":
            producto_reponer = input("Ingrese el nombre del producto a reponer: ").strip()
            if producto_reponer.capitalize() in herramientas:
              indice = herramientas.index(producto_reponer.capitalize())
              can_reponer = input("Ingrese la cantidad a reponer: ").strip()
              if can_reponer.isdigit() and int(can_reponer) > 0:
                existencias[indice] += int(can_reponer)
                print(f"Se sumo {int(can_reponer)} unidades del producto {herramientas[indice]}")
                print(f"Stock actual : {existencias[indice]}")
                break
              else:
                print("Error cantidad mal ingresada(solo numeros) ")
            else:
              print("El producto no esta en la lista")
          else:
            print("Ingrese un numero dentro de las opciones (1 o 2)")
        else:
          print("Ingrese un numero correcto")
    else:
      print("Aun no se inicializo la lista...")
  elif opcion == "8":
    print("Saliendo del programa")
    break
  else:
    print("Ingrese una opción correcta...")
