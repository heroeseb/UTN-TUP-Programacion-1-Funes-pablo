from fcs_clase_11_05 import *

lista = cargar_archivo()

while True:
    menu()
    opcion = input_int('Ingrese una opcion (1-7): ','Ingrese solamente numeros!')
    match opcion:
        case 1:
            print("Elegiste: Agregar libro")
            print(lista)
        case 2:
            print("Elegiste: Mostrar libros")
        case 3:
            print("Elegiste: Buscar libro")
        case 4:
            print("Elegiste: Modificar libro")
        case 5:
            print("Elegiste: Eliminar libro")
        case 6:
            print("Elegiste: Estadísticas")
        case 7:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción inválida. Intente nuevamente.")
