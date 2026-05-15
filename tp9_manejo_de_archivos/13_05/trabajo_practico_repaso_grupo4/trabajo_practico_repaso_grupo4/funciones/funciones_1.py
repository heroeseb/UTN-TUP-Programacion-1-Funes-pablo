def calcular_promedio(lista):
  if not lista:
    print("La lista se encuentra vacia.")
    return 0
  else:
    promedio = sum(lista) / len(lista)
    return promedio