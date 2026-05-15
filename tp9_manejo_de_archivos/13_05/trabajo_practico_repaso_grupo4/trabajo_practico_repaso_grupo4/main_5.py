from trabajo_practico_repaso.funciones.funciones_5 import *
productos = cargar_archivo()
while True:
    menu()
    print()
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            productos = añadir_producto(productos)
        case "2":
            mostrar_productos(productos)
        case "3":
            buscar_productos(productos)
        case "4":
            estadisticas(productos)
        case "5":
            print("Muchas gracias por usar el sistema!! Hasta luego.")
            break
        case _:
            print("Error... Comando incorrecto, intente nuevamente.")