from funciones.funciones_csv_eic import *
from funciones.funciones_impresion_eic import *
from funciones.funciones_productos_eic import *

productos = cargar_productos()

while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")
  if opcion == "1":
    productos = agregar_producto(productos)
  elif opcion == "2":
    mostrar_productos(productos)
  elif opcion == "3":
    buscar_producto(productos)
  elif opcion == "4":
    productos = modificar_producto(productos)
  elif opcion == "5":
    productos = eliminar_producto(productos)
  elif opcion == "6":
    estadisticas_productos(productos)
  elif opcion == "7":
    guardar_productos(productos)
    print("¡Hasta luego!")
    break
  else:
    print("Opción no válida. Intente nuevamente.")