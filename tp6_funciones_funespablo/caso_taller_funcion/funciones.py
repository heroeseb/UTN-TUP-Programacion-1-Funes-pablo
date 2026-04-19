def mostrar_menu():
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

def caso_1(ordenes,horas):
    ordenes_caso1 = ordenes.copy()
    horas_caso1 = horas.copy()
    int_cant_ordenes = input_int("Ingrese la cantidad de ordenes a ingresar: ")
    for _ in range(int_cant_ordenes):
        orden_agre,horas_agre = agregar_orden(ordenes_caso1)
        ordenes_caso1 = ordenes_caso1 + orden_agre
        horas_caso1 = horas_caso1 + horas_agre
    return ordenes_caso1,horas_caso1

def es_entero(dato):
    if dato.isdigit() and int(dato) > 0:
        return True
    else:
        return False

def input_int(mensaje):
    while True:
        numero = input_mensaje(mensaje)
        if es_entero(numero):
            numero = int(numero)
            return numero
        else:
            print("Ingrese un numero correcto...")

def validar_no_esta_ord(dato,lista):
    if (dato.startswith("ORD-") or dato.startswith("ord-")) and dato[4:].isdigit() and len(dato[4:]) == 3 and (dato.upper() not in lista):
        return True
    else:
        return False

def agregar_orden(ordenes):
    while True:
        orden_agregar = []
        hora_agregar = []
        orden = input_mensaje("Dime el numero de orden.ej('ORD-004'): ")
        if validar_no_esta_ord(orden,ordenes):
            orden_agregar.append(orden.upper())
            hora_agregar.append(0)
            print(f"Orden {orden.upper()} ingresada correctamente (se le asiganara 0 como valor por defecto)")
            return orden_agregar,hora_agregar
        else:
            print("Ingrese una orden correcta o no repetida.ej('ORD-004')")

def caso2(ordenes,horas):
    ordenes_caso2 = ordenes.copy()
    horas_caso2 = horas.copy()
    if ordenes and horas:
        for i in range(len(ordenes_caso2)):
            while True:
                hora_est = input_mensaje(f"Dime las horas estimada para {ordenes_caso2[i]} (las horas estimadas actuales son {horas_caso2[i]}): ")
                if hora_est.replace(".","").isdigit():
                    horas_caso2[i] = float(hora_est)
                    print(f"Hora de orden {ordenes[i]} modificada correctamente!")
                    break
                else:
                    print("Ingrese un numero correcto de horas...")
        return ordenes_caso2,horas_caso2

def input_mensaje(mensaje):
    input_resultado = input(mensaje).strip()
    return input_resultado

def caso3(ordenes,horas):
    if ordenes and horas and len(ordenes) == len(horas):
        ordenes_caso3 = ordenes.copy()
        horas_caso3 = horas.copy()
        print("Agenda del taller: ")
        for i in range(len(ordenes_caso3)):
            print(f"Orden: {ordenes_caso3[i]}, tiempo estimado de {horas_caso3[i]} horas")
    else:
        print("Aun no se ha inicializado la lista o estan desincronizadas...")

def caso4(ordenes,horas):
    while True:
        num_orden = input_mensaje("Ingrese el numero de orden que desea buscar las horas estimadas: ").upper()
        if num_orden in ordenes:
            print(f"Orden: {ordenes[ordenes.index(num_orden)]} , tiempo estimado de {horas[ordenes.index(num_orden)]} horas.")
            break
        else:
            print("El numero de orden no esta en la lista o esta mal escrito.")

def caso5(ordenes,horas):
    if 0 not in horas:
        print("No hay ordenes pendientes de diagnostico!")
    else:
        print("Ordenes pendientes de diagnostico: ")
        for i in range(len(ordenes)):
            if horas[i] <= 0:
                print(f"- Orden: {ordenes[i]}, pendiente de diagnostico.")

def caso6(ordenes,horas):
    ordenes_caso6 = ordenes.copy()
    horas_caso6 = horas.copy()
    while True:
        orden_agregar = input_mensaje("Dime el numero de orden a ingresar: ").upper()
        if validar_no_esta_ord(orden_agregar,ordenes_caso6):
            hora_estipulada = input_mensaje("Dime la cantidad de horas estimadas: ")
            if es_entero(hora_estipulada):
                ordenes_caso6.append(orden_agregar)
                horas_caso6.append(float(hora_estipulada))
                print(f"Orden {orden_agregar} se agrego con exito...")
                return ordenes_caso6,horas_caso6
            else:
                print("Ingrese un numero correcto...")
        else:
            print("La orden ya esta en la lista / ingrese un numero de orden correcto...")

def caso7(ordenes,horas):
    while True:
        ordenes_caso7 = ordenes.copy()
        horas_caso7 = horas.copy()
        orden_modificar = input_mensaje("Ingrese la orden a la que actualizar las horas: ").upper()
        if (orden_modificar.startswith("ORD-") or orden_modificar.startswith("ord-")) and orden_modificar[4:].isdigit() and len(orden_modificar[4:]) == 3 and (orden_modificar in ordenes_caso7):
            horas_modificado = input_mensaje("Ingrese la cantidad de horas estimadas: ")
            if es_entero(horas_modificado):
                index_orden = ordenes_caso7.index(orden_modificar)
                horas_caso7[index_orden] = float(horas_modificado)
                print(f"Orden {orden_modificar} modificada correctamente.")
                return ordenes_caso7,horas_caso7
            else:
                print("Ingrese un numero correcto...")
        else:
            print("Ingrese una orden correcta...")