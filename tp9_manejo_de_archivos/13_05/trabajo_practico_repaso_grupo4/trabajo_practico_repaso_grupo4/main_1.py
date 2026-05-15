from funciones.funciones_1 import *

print("Ejercicio 1")

numeros = []

for i in range(5):
  while True:
    try:
      numero = float(input(f"Ingrese el numero {i + 1}: "))
      numeros.append(numero)
      break
    except ValueError:
      print("Debe ingresar un numero.")

promedio = calcular_promedio(numeros)

if promedio != 0:
  print(f"El promedio de los numeros ingresados es: {promedio:.2f}")

print(f"El mayor numero ingresado es: {max(numeros)}")
print(f"El menor numero ingresado es: {min(numeros)}")