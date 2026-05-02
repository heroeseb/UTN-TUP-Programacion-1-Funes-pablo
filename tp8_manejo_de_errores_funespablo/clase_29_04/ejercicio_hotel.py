from fcs_hotel import *
from excepciones_hotel import HabitacionExistenteError, HabitacionNoEncontradaError

habitaciones = []

while True:
    mostrar_menu()
    
    opcion = input('Seleccione una opción: ')
    
    try:
        if opcion == '1':
            agregar_habitacion(habitaciones)
        elif opcion == '2':
            mostrar_habitaciones(habitaciones)
        elif opcion == '3':
            consultar_habitacion(habitaciones)
        elif opcion == '4':
            cambiar_estado(habitaciones)
        elif opcion == '5':
            listar_por_estado(habitaciones)
        elif opcion == '6':
            print('Hasta luego!')
            break
        else:
            print('Opción inválida.')
    
    except HabitacionExistenteError as e:
        print(e)
    except HabitacionNoEncontradaError as e:
        print(e)