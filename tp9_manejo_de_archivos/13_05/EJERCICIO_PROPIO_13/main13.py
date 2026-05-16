from fcs_13 import *

productos = cargar_datos(csv_productos)

while True:
    menu()
    opcion = input_int_or_float('int','Ingrese una opción: ')
    match opcion:
        case 1:
            producto = agregar_producto(productos)
            productos.append(producto)
            guardar_datos(productos)
        case 2:
            mostrar_productos(productos)
        case 3:
            buscar_producto(productos)
        case 4:
            productos = modificar_producto(productos)
            guardar_datos(productos)
        case 5:
            productos = eliminar_producto(productos)
            guardar_datos(productos)
        case 6:
            mostrar_estadisticas(productos)
        case 7:
            print('Saliendo del programa')
            break
        case _:
            print('Ingrese una opcion correcto!')