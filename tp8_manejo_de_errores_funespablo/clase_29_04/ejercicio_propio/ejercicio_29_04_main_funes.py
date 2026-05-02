from fcs_clase_29_04_funes import *

habitaciones = []

while True:
    print('''
        1. Agregar habitación
        2. Mostrar todas las habitaciones
        3. Consultar una habitación
        4. Cambiar estado de una habitación
        5. Listar habitaciones libres u ocupadas
        6. Salir
        ''')
    opcion = validar_input_numero('Ingrese una opción: ','Ingrese un numero correcto!')
    match opcion:
        case 1:
            habitaciones = caso_1(habitaciones)
        case 2:
            if not habitaciones:
                print('Aun no se inicializa la lista')
            else:
                caso_2(habitaciones)
        case 3:
            caso_3(habitaciones)
        case 4:
            habitaciones = caso_4(habitaciones)
        case 5:
            if not habitaciones:
                print('Lista aun no se ha inicializado')
            else:
                caso_5(habitaciones)
        case 6:
            print('Saliendo del programa...')
            break
        case _:
            print('Ingrese una opción correcta!')


print(habitaciones)