# Funes Pablo Sebastian
ordenes= ["ORD-001", "ORD-002", "ORD-003"]
horas= [2.5, 0, 4.0]

while True:
    print("""
        1. Ingresar órdenes (códigos): (Registrar las órdenes de reparación en el sistema)
        2. Ingresar horas estimadas por orden: (Definir el tiempo estimado inicial para cada orden)
        3. Mostrar agenda del taller: (Mostrar todas las órdenes y sus tiempos estimados)
        4. Consultar horas por orden: (Verificar el tiempo estimado para una orden específica)
        5. Listar órdenes con 0 horas (pendiente de diagnóstico): (Mostrar las órdenes que requieren diagnóstico)
        6. Agregar orden: (Añadir una nueva orden al sistema)
        7. Actualizar horas: (Modificar el tiempo estimado de una orden)
        8. Salir
        """)
    opcion = input("Elija una opción: ")
    match opcion:
        case "1":
            while True:
                cant_ordenes = input("Ingrese la cantidad de ordenes a ingresar: ").strip()
                if cant_ordenes.isdigit() and int(cant_ordenes) > 0:
                    int_cant_ordenes = int(cant_ordenes)
                    for i in range(int_cant_ordenes):
                        while True:
                            orden = input("Dime el numero de orden.ej('ORD-004'): ").strip()
                            if (orden.startswith("ORD-") or orden.startswith("ord-")) and orden[4:].isdigit() and (orden not in ordenes):
                                ordenes.append(orden.upper())
                                horas.append(0)
                                print(f"Orden {orden.upper()} ingresada correctamente (se le asiganara 0 como valor por defecto)")
                                break
                            else:
                                print("Ingrese una orden correcta o no repetida.ej('ORD-004')")
                    break
                else:
                    print("Ingrese un numero correcto..")
        case "2":
            if ordenes and horas:
                for i in range(len(ordenes)):
                    while True:
                        hora_est = input(f"Dime las horas estimada para {ordenes[i]} (las horas estimadas actuales son {horas[i]}): ").strip()
                        if hora_est.replace(".","").isdigit():
                            horas[i] = float(hora_est)
                            print(f"Hora de orden {ordenes[i]} modificada correctamente!")
                            break
                        else:
                            print("Ingrese un numero correcto de horas...")
        case "3":
            print("Agenda del taller: ")
            for i in range(len(ordenes)):
                print(f"Orden: {ordenes[i]}, tiempo estimado de {horas[i]} horas")
        case "4":
            while True:
                num_orden = input("Ingrese el numero de orden que desea buscar las horas estimadas: ").strip()
                num_orden = num_orden.upper()
                if num_orden in ordenes:
                    print(f"Orden: {ordenes[ordenes.index(num_orden)]} , tiempo estimado de {horas[ordenes.index(num_orden)]} horas.")
                    break
                else:
                    print("El numero de orden no esta en la lista o esta mal escrito.")
        case "5":
            if 0 not in horas:
                print("No hay ordenes pendientes de diagnostico!")
            else:
                print("Ordenes pendientes de diagnostico: ")
                for i in range(len(ordenes)):
                    if horas[i] <= 0:
                        print(f"- Orden: {ordenes[i]}, pendiente de diagnostico.")
        case "6":
            while True:
                orden_agregar = input("Dime el numero de orden a ingresar: ").strip()
                if orden_agregar.startswith("ORD-") and orden_agregar[4:].isdigit() and (orden_agregar not in ordenes):
                    hora_estipulada = input("Dime la cantidad de horas estimadas: ").strip()
                    if hora_estipulada.replace(".","").isdigit():
                        ordenes.append(orden_agregar)
                        horas.append(float(hora_estipulada))
                        print(f"Orden {orden_agregar} se agrego con exito...")
                        break
                    else:
                        print("Ingrese un numero correcto...")
                else:
                    print("La orden ya esta en la lista / ingrese un numero de orden correcto...")
        case "7":
            while True:
                orden_modificar = input("Ingrese la orden a la que actualizar las horas: ")
                if (orden_modificar.startswith("ORD-") or orden_modificar.startswith("ord-")) and orden_modificar[4:].isdigit() and (orden_modificar.upper() in ordenes):
                    horas_modificado = input("Ingrese la cantidad de horas estimadas: ").strip()
                    if horas_modificado.replace(".","").isdigit():
                        orden_modificar = orden_modificar.upper()
                        index_orden = ordenes.index(orden_modificar)
                        horas[index_orden] = float(horas_modificado)
                        print(f"Orden {orden_modificar} modificada correctamente.")
                        break
                    else:
                        print("Ingrese un numero correcto...")
                else:
                    print("Ingrese una orden correcta...")
        case "8":
            print("Saliendo del programa")
            break
        case _:
            print("Elija una opción correcta...")





