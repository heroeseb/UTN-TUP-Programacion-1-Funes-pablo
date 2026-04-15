from fcs_hotel import *
# import fcs_hotel

habitaciones = ["101"]
estados = [0]

while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    match opcion:
        case '1':
            opcion_uno(habitaciones, estados)
        case '2':
            opcion_dos(habitaciones, estados)
        case '3':
            opcion_tres(habitaciones, estados)
        case '4':
            opcion_cuatro(habitaciones, estados)
        case '5':
            opcion_cinco(habitaciones, estados)
        case '6':
            opcion_seis(habitaciones, estados)
        case '7':
            opcion_siete(habitaciones, estados)
        case '8':
            print("Saliendo del programa...")
            break
        case _:
            print("Error: Opción inválida. Intente de nuevo.")