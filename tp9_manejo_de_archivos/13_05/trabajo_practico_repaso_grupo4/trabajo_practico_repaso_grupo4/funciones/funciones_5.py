from trabajo_practico_repaso.funciones.funciones_validar_5 import *
from trabajo_practico_repaso.funciones.funciones_guardado_5 import *
def menu():
    print("==============BIENVENIDO/A A LA BIBLIOTECA DE LA TIERRA MEDIA==================")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Estadísticas")
    print("5. Salir")


def añadir_producto(lista):
    producto=validar_texto("Ingrese el nombre del producto: ")
    if producto in [producto["producto"] for producto in lista]:
        print("El producto ya está cargado en el sistema.")
        print("Volviendo al menú...")
        print()
        return lista
    else:
      print("Agregando producto...")
      id=None
      precio=validar_flotante("Ingrese el precio del producto: ")
      nuevo_producto={"producto":producto, "precio":precio}
      lista.append(nuevo_producto)
      guardar_archivo(lista)
    return lista

def mostrar_productos(lista):
    if lista:
        for p in lista:
            print("-" * 40)
            print(f"""-Producto: {p['producto']} 
-Precio: ${p['precio']}""")
            print("-" * 40)
    else:
      print("No hay productos cargados en el sistema actualmente.")

def buscar_productos(lista):
    busqueda = validar_texto("Ingrese el nombre del producto que desea buscar: ")
    encontrado = False
    for producto in lista:
        if producto["producto"].lower() == busqueda.lower():
            mostrar_productos([producto])
            encontrado = True
            break
    if not encontrado:
        print(f"El producto '{busqueda}' no se encuentra cargado en el sistema actualmente.")

def estadisticas(lista):
    if lista:
        total_productos = len(lista)
        promedio = sum(p["precio"] for p in lista) / total_productos
        precio_mas_alto = max(p["precio"] for p in lista)
        precio_mas_bajo = min(p["precio"] for p in lista)
        print(f"""== ESTADÍSTICAS DE LOS PRODUCTOS ==
- Total de productos en el sistema: {total_productos}
- Promedio de precios de productos actualmente: ${promedio:.2f}
- Producto más caro del sistema: ${precio_mas_alto:.2f}
- Producto más barato del sistema: ${precio_mas_bajo:.2f}""")
    else:
        print("No hay productos en el sistema para mostrar estadísticas.")