def mostrar_menu():
  print("== Sistema de gestión de productos ==")
  print("> 1. Agregar producto")
  print("> 2. Mostrar productos")
  print("> 3. Buscar producto (por ID o nombre)")
  print("> 4. Modificar producto")
  print("> 5. Eliminar producto")
  print("> 6. Estadísticas de productos")
  print("> 7. Salir")

def mostrar_productos(productos):
  if productos:
    print("-" * 40)
    for p in productos:
      print(f"[{p["id"]}] Nombre: {p["nombre"]} | Categoría: {p["categoria"]} | Precio: {p["precio"]} | Stock: {p["stock"]}")
    print("-" * 40)
  else:
    print("No hay productos cargados en el sistema actualmente.")

def mostrar_producto(producto):
  print("-" * 40)
  print(f"[{producto["id"]}] Nombre: {producto["nombre"]} | Categoría: {producto["categoria"]} | Precio: {producto["precio"]} | Stock: {producto["stock"]}")
  print("-" * 40)