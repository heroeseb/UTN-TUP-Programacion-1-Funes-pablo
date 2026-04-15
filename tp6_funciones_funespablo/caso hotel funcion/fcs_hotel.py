def mostrar_menu():
    print("\n--- MENÚ HOTEL ---")
    print("1. Ingresar números de habitación")
    print("2. Ingresar estados (0/1) paralelos")
    print("3. Mostrar estado general")
    print("4. Consultar estado de una habitación")
    print("5. Listar ocupadas o libres")
    print("6. Agregar habitación")
    print("7. Cambiar estado")
    print("8. Salir")

def opcion_uno(habitaciones, estados):

    cantidad_int = validar_entero('Ingrese cuantas habitaciones desea agregar: ')
    
    print(f"Ingrese los {cantidad_int} números de habitación:")
    
    for i in range(cantidad_int):
        hab = validar_entero('Ingrese el número de habitación: ')

        if not dato_existente(hab, habitaciones):
            habitaciones.append(hab)
            estados.append(0)

def opcion_dos(habitaciones, estados):
    if not exsistencias(habitaciones):
        for i in range(len(habitaciones)):
            while True:
                estado = input(f"Ingrese estado para la habitación {habitaciones[i]} (0=Libre, 1=Ocupada): ")
                if estado == '0' or estado == '1':
                    estados[i] = int(estado)
                    break
                else:
                    print("Error: Estado inválido. Debe ingresar 0 o 1.")

def opcion_tres(habitaciones, estados):
    if not exsistencias(habitaciones):
        for i in range(len(habitaciones)):
            if estados[i] == 0:
                estado_str = "Libre"
            elif estados[i] == 1:
                estado_str = "Ocupada"
            print(f"Habitación {habitaciones[i]}: {estado_str}")

def opcion_cuatro(habitaciones, estados):
    if not exsistencias(habitaciones):
        hab = input("Ingrese el número de la habitación a consultar: ")
        if dato_existente(hab, habitaciones):
            idx = habitaciones.index(hab)
            if estados[idx] == 0:
                print(f"Habitación {hab}: Libre")
            elif estados[idx] == 1:
                print(f"Habitación {hab}: Ocupada")
        else:
            print("Error: La habitación no existe.")

def opcion_cinco(habitaciones, estados):
    if not exsistencias(habitaciones):
        filtro = input("Ingrese 0 para ver habitaciones Libres o 1 para Ocupadas: ")
        if filtro == '0' or filtro == '1':
            filtro_int = int(filtro)
            encontradas = False
            for i in range(len(habitaciones)):
                if estados[i] == filtro_int:
                    if filtro_int == 0:
                        estado_str = "Libre"
                    else:
                        estado_str = "Ocupada"
                        
                    print(f"Habitación {habitaciones[i]}: {estado_str}")
                    encontradas = True
            
            if not encontradas:
                print("No se encontraron habitaciones bajo ese criterio.")
        else:
            print("Error: Opción inválida.")

def opcion_seis(habitaciones, estados):
    hab = validar_entero("Ingrese el número de la nueva habitación: ")
    if not dato_existente1(hab,habitaciones):
        while True:
            estado = input("Ingrese el estado (0=Libre, 1=Ocupada): ")
            if estado == '0' or estado == '1':
                habitaciones.append(hab)
                estados.append(int(estado))
                print("Habitación agregada con éxito.")
                break
            else:
                print("Error: Estado inválido.")

def opcion_siete(habitaciones, estados):
    if not exsistencias(habitaciones):
        hab = input("Ingrese el número de la habitación a modificar: ")
        if dato_existente(hab, habitaciones):
            idx = habitaciones.index(hab)
            while True:
                nuevo_estado = input("Ingrese el nuevo estado (0=Libre, 1=Ocupada): ")
                if nuevo_estado == '0' or nuevo_estado == '1':
                    estados[idx] = int(nuevo_estado)
                    print("Estado modificado con éxito.")
                    break
                else:
                    print("Error: Estado inválido.")

def exsistencias(habitaciones):
    if not habitaciones:
        print("No hay datos registrados.")
        return True
    return False

def validar_entero(msj):
    while True:
        n_str = input(msj)
        if n_str.isdigit() and int(n_str) > 0:
                n_int = int(n_str)
                return n_int
        else:
            print("Error: Por favor ingrese un número entero mayor a 0.")

def dato_existente(msj, lista):
    while True:
        dato = validar_entero("Ingrese el número de la nueva habitación: ")
        if dato in lista:
            print("El dato existe en la lista.")
            return True

def dato_existente1(dato,lista):
    if dato in lista:
        print("El dato existe en la lista.")
        return True