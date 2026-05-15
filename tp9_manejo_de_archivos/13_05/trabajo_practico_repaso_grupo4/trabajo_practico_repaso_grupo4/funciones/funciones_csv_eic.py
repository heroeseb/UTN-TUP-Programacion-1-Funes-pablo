import csv

def cargar_productos():
  productos = []
  try:
    with open("productos.csv", "r", encoding="utf-8") as archivo:
      reader = csv.DictReader(archivo)
      filas_invalidas = []
      for numero_linea, row in enumerate(reader, start=2):
        try:
          id = int(row["id"])
          nombre = row["nombre"].strip().capitalize()
          categoria = row["categoria"].strip().capitalize()
          precio = float(row["precio"])
          stock = int(row["stock"])
          if not nombre or not categoria:
            raise ValueError("Nombre o categoria vacios.")
          if precio <= 0 or stock < 0:
            raise ValueError("Precio o stock no validos.")
          producto = {
            "id": id,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "stock": stock
          }
          productos.append(producto)
        except (ValueError, TypeError, KeyError):
          filas_invalidas.append(numero_linea)
      if filas_invalidas:
        print(f"Se omitieron {len(filas_invalidas)} fila(s) invalidas del CSV: {', '.join(map(str, filas_invalidas))}")
  except FileNotFoundError:
    print("Archivo 'productos.csv' no encontrado. Se cargará un catalogo inicial.")
  except Exception as e:
    print(f"Ha ocurrido un error al cargar los datos: {e}")
  return productos

def guardar_productos(productos):
  try:
    with open("productos.csv", "w", newline="", encoding="utf-8") as archivo:
      fieldnames = ["id", "nombre", "categoria", "precio", "stock"]
      writer = csv.DictWriter(archivo, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(productos)
  except Exception as e:
    print(f"Ha ocurrido un error al guardar los datos: {e}")