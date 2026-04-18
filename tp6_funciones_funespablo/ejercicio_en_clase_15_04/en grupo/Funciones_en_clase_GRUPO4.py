#FUNCIONES DE CÁLCULO
def calcular_promedio(notas):
    return sum(notas)/len(notas)
def nota_maxima(notas):
  return max(notas)
def nota_minima(notas):
  return min(notas)

#FUNCIÓN DE FILTRO
def filtrar_aprobados(numeros, umbral = 6):
  return [num for num in numeros if num >= umbral]

#FUNCIÓN DE IMPRESIÓN
def analizar_notas(notas):
  print(f"Promedio: {calcular_promedio(notas)}")
  print(f"Nota más alta: {nota_maxima(notas)}")
  print(f"Nota más baja: {nota_minima(notas)}")