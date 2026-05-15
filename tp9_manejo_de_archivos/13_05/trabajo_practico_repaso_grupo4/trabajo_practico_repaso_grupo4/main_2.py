from funciones.funciones_2 import *

print("Ejercicio 2")

contrasena = input("Ingrese una contraseña: ").strip()
if validar_contrasena(contrasena):
  print("La contraseña es válida.")
else:
  print("La contraseña no es válida. Debe tener al menos 8 caracteres y contener al menos un número.")