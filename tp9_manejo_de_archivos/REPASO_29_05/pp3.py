def validar_texto(mensaje1):
    while True:
        try:
            texto = input(mensaje1).capitalize()
            if texto.replace(" ","").isalpha():
                return texto
        except ValueError:
            print("Error... Ingreso incorrecto.")
        except Exception as e:
            print(f"Error: {e}")
def validar_entero(mensaje1):
    while True:
        try:
            numero = int(input(mensaje1).strip())
            if numero or numero == 0:
                return numero
        except ValueError:
            print("Error... Ingreso incorrecto.")
        except Exception as e:
            print(f"Error: {e}")

#==================================================================================================#
def agregar_herramienta(lista,cantidad):
    for i in range(cantidad):
        herramienta=validar_texto(f"Ingrese el nombre de la herramienta n°{i+1}: ")
        if [p for p in lista if herramienta == p["herramienta"]]:
            print("Error... La herramienta ya existe en el catálogo.")
            continue
        unidades=validar_entero(f"Ingrese la cantidad de unidades de '{herramienta}': ")
        lista.append({"herramienta":herramienta,"unidades":unidades})
        print("Herramienta agregada exitosamente.")
        print()
    return lista
def modificar_dato(lista):
    if not lista:
        print("Error... La lista se encuentra vacía.")
        print()
        return lista
    buscar=validar_texto("Ingrese el nombre de la herramienta que desea buscar: ")
    encontrado=False
    for p in lista:
        if buscar.lower() == p["herramienta"].lower() :
            cantidad_nueva = validar_entero(f"Ingrese las unidades de '{buscar}' actualizadas: ")
            p["unidades"] = cantidad_nueva
            print("Cambio realizado exitosamente.")
            print()
            encontrado=True
            return lista
    if not encontrado:
        print(f"La herramienta '{buscar}' no se encontró registrada.")
        print()
        return lista
def mostrar_herramienta(lista):
    if not lista:
        print("Error... La lista se encuentra vacía.")
        print()
        return lista
    for p in lista:
        print(f"""Herramienta: {p["herramienta"]}
Unidades: {p["unidades"]}""")
        print()
def buscar_herramienta(lista):
    if not lista:
        print("Error... La lista se encuentra vacía.")
        return lista
    print()
    buscar=validar_texto("Ingrese el nombre de la herramienta que desea buscar: ")
    encontrado=False
    for p in lista:
        if buscar.lower()  == p["herramienta"].lower() :
            print(f"""Herramienta: {p["herramienta"]}
Unidades: {p["unidades"]}""")
            encontrado=True
            print()
    if not encontrado:
        print(f"La herramienta '{buscar}' no se encontró registrada.")
        print()
        return lista
def agotados(lista):
    if not lista:
        print("Error... La lista se encuentra vacía.")
        print()
        return lista
    encontrado=False
    for p in lista:
        if p["unidades"]==0:
            print(f"""Herramienta: {p["herramienta"]}
    Unidades: {p["unidades"]}""")
            encontrado=True
            print()
    if not encontrado:
        print("Actualmente no hay herramientas agotadas.")
        print()
def prestar_devolver(lista):
    if not lista:
        print("Error... La lista se encuentra vacía.")
        print()
        return lista
    buscar=validar_texto("Ingrese el nombre de la herramienta que desea buscar: ")
    for p in lista:
        if buscar.lower()  == p["herramienta"].lower() :
            while True:
                opcion=input(f""" Herramienta '{buscar}'
    ¿Qué desea hacer?
                             
1- Prestar
2- Devolver
3- Salir
            
    - """)
                match opcion:
                    case "1":
                        if p["unidades"] <= 0:
                            print("No se puede hacer el préstamo, no hay unidades suficientes.")
                            print()
                        else:
                            p["unidades"] -= 1
                            print(f"Se ha prestado una unidad de {p["herramienta"]}.")
                            print()
                            return lista
                    case "2":
                        p["unidades"] += 1
                        print(f"Se ha devuelto una unidad de {p["herramienta"]}.")
                        print()
                        return lista
                    case "3":
                        print("Volviendo al menú principal...")
                        print()
                        break
                    case _:
                        print("Error... Comando incorrecto.")
                        print()
        else:
            print(f"La herramienta '{buscar}' no se encontró registrada.")
            print()
            return lista

#============================================================================================================

herramientas=[{"herramienta":"Martillo","unidades":3},{"herramienta":"Cinta","unidades":0}]
while True:
    opcion=input(""" | MENÚ DE GESTIÓN 'Ferretería Don Pepe' | 

- Acciones -
1- Agregar herramientas
2- Modificar herramienta
3- Mostrar catálogo
4- Buscar herramienta
5- Mostrar agotados
6- Agregar herramienta (Unidad)
7- Préstamo o Devolución
8- Salir
            
    - """)
    print()
    match opcion:
        case "1" | "uno":
            cantidad=validar_entero("Cuantas herramientas va a añadir al sistema?: ")
            print()
            agregar_herramienta(herramientas,cantidad)
        case "2" | "dos":
            modificar_dato(herramientas)
        case "3" | "tres":
            mostrar_herramienta(herramientas)
        case "4" | "cuatro":
            buscar_herramienta(herramientas)
        case "5" | "cinco":
            agotados(herramientas)
        case "6" | "seis":
            agregar_herramienta(herramientas,1)
        case "7" | "siete":
            prestar_devolver(herramientas)
        case "8" | "ocho":
            print("Muchas gracias por usar el sistema! Hasta luego.")
            break
        case _:
            print("Error... Comando incorrecto.")