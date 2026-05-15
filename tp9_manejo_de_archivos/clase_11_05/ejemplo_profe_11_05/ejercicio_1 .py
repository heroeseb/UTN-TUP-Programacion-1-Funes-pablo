from fcs_ej_1 import *

estudiantes = cargar_archivo()

while True:
    
    mostrar_menu()
    
    opcion = input('Ingrese un opción: ')
    
    match opcion:
        case '1':
            estudiantes = agregar_estudiante(estudiantes)
        case '2':
            mostrar_estudiantes(estudiantes)
        case '3':
            guardar_archivo(estudiantes)
        case '4':
            estadisticas(estudiantes)
        case '5':
            print('Hasta luego')
            break
        case _:
            print('Opción incorrecta.')