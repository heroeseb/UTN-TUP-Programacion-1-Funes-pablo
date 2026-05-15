from funciones.funciones_validacion_eic import *
from funciones.funciones_csv_eic import *
from funciones.funciones_impresion_eic import *

def generar_id(productos):
  if not productos:
    return 0
  else:
    return max(producto['id'] for producto in productos) + 1

def agregar_producto(productos):
  id = generar_id(productos)
  nombre = validacion_texto("Ingrese el nombre del producto: ", None).capitalize()
  if nombre.lower() in (p['nombre'].lower() for p in productos):
    print("ERROR! Ya existe un producto con ese nombre.")
    return productos
  else:
    categoria = validacion_texto("Ingrese la categoría del producto: ", None).capitalize()
    precio = validacion_float("Ingrese el precio del producto: ", None, True)
    stock = validacion_entero("Ingrese el stock del producto: ", None, True)
  
  productos.append(
    {
      "id": id,
      "nombre": nombre,
      "categoria": categoria,
      "precio": precio,
      "stock": stock
    }
  )
  print("Producto agregado exitosamente.")
  guardar_productos(productos)
  return productos

def buscar_producto(productos):
  if productos:
    while True:
      opcion = input("¿Desea buscar por ID (1) o por nombre (2)? ")
      if opcion == "1":
        busqueda = validacion_entero("Ingrese la ID del productos que desea buscar: ")
        resultado = [p for p in productos if busqueda == p["id"]]
        if resultado:
          mostrar_productos(resultado)
        else:
          print("No se han encontrado productos que coincidan con la búsqueda.")
        break
      else:
        busqueda = validacion_texto("Ingrese el nombre del productos que desea buscar: ")
        resultado = [p for p in productos if busqueda.lower() == p["nombre"].lower()]
        if resultado:
          mostrar_productos(resultado)
        else:
          print("No se han encontrado productos que coincidan con la búsqueda.")
        break
  else:
    print("No hay productos cargados en el sistema actualmente.")

def modificar_producto(productos):
  if productos:
    busqueda = validacion_texto("Ingrese el nombre del productos que desea modificar: ")
    while True:
      opcion = input("¿Qué desea modificar? - Nombre (1) - Categoría (2) - Precio (3) - Stock (4): ")
      if opcion == "1":
        nuevo_nombre = validacion_texto("Ingrese el nuevo nombre del producto: ").capitalize()
        if nuevo_nombre.lower() in (p["nombre"].lower() for p in productos):
          print("ERROR! Ya existe un producto con ese nombre.")
          break
        else:
          for p in productos:
            if busqueda.lower() == p["nombre"].lower():
              p["nombre"] = nuevo_nombre
              print("Producto modificado exitosamente.")
              guardar_productos(productos)
              return productos
      elif opcion == "2":
        nueva_categoria = validacion_texto("Ingrese la nueva categoría del producto: ").capitalize()
        for p in productos:
          if busqueda.lower() == p["nombre"].lower():
            p["categoria"] = nueva_categoria
            print("Producto modificado exitosamente.")
            guardar_productos(productos)
            return productos
      elif opcion == "3":
        nuevo_precio = validacion_float("Ingrese el nuevo precio del producto: ", None, True)
        for p in productos:
          if busqueda.lower() == p["nombre"].lower():
            p["precio"] = nuevo_precio
            print("Producto modificado exitosamente.")
            guardar_productos(productos)
            return productos
      elif opcion == "4":
        nuevo_stock = validacion_entero("Ingrese el nuevo stock del producto: ", None, True)
        for p in productos:
          if busqueda.lower() == p["nombre"].lower():
            p["stock"] = nuevo_stock
            print("Producto modificado exitosamente.")
            guardar_productos(productos)
            return productos
  else:
    print("No hay productos cargados en el sistema actualmente.")

def eliminar_producto(productos):
  if productos:
    busqueda = validacion_texto("Ingrese el nombre del productos que desea eliminar: ")
    for p in productos:
      if busqueda.lower() == p["nombre"].lower():
        productos.remove(p)
        print("Producto eliminado exitosamente.")
        guardar_productos(productos)
        return productos
    print("No se han encontrado productos que coincidan con la búsqueda.")
  else:
    print("No hay productos cargados en el sistema actualmente.")

def estadisticas_productos(productos):
  if productos:
    total_productos = len(productos)
    precio_mas_alto = max(p["precio"] for p in productos)
    promedio = sum(p["precio"] for p in productos) / total_productos
    stock_total = sum(p["stock"] for p in productos)
    print(f"""== ESTADÍSTICAS DE LOS PRODUCTOS ==
- Total de productos en el sistema: {total_productos}
- Producto más caro del sistema: ${precio_mas_alto:.2f}
- Promedio de precios de productos actualmente: ${promedio:.2f}
- Stock total de productos del sistema: {stock_total}""")
  else:
    print("No hay productos cargados en el sistema actualmente.")