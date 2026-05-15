import csv
def cargar_archivo():
  lista = []
  try:
    with open("productos_5.csv", "r", encoding="utf-8") as archivo:
      reader = csv.DictReader(archivo)
      for fila in reader:
        lista.append({
            "producto": fila["producto"],
            "precio": float(fila["precio"]),
        }) 
    print("Archivo cargado exitosamente.")
  except FileNotFoundError:
    print("El archivo no existe. Se creará una lista vacía.")
  except PermissionError:
    print("Error... No tenes permiso de lectura en este archivo.")
  return lista

def guardar_archivo(lista):
  try:
    with open("productos_5.csv", "w", newline="", encoding="utf-8") as archivo:
      fieldnames = ["producto", "precio"]
      writer = csv.DictWriter(archivo, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(lista)
    print("Archivo guardado exitosamente.")
  except FileNotFoundError:
    print("El archivo no existe.")
  except PermissionError:
    print("Error... No tiene permiso para escritura.")