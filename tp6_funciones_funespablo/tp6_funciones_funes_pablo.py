# Alumno : Funes Pablo Sebastian

# Funciones para validar datos:

def es_flotante(numero):
    if numero.replace(".","").isdigit() and numero.count(".") <= 1:
        return True
    else:
      return False

def input_float(mensaje):
  while True:
    float_input = input(f"{mensaje}").strip()
    if es_flotante(float_input):
      return float(float_input)
    else:
      print("Ingrese un número correcto!")

def input_entero(mensaje):
  while True:
    entero_input = input(f"{mensaje}").strip()
    if entero_input.isdigit():
      return int(entero_input)
    else:
      print("Ingrese un número correcto!")

# 1. Función Hola Mundo!.
print("--- Ejercicio 1: Función Hola Mundo ---")

def imprimir_hola_mundo():
  print("¡Hola Mundo!")

imprimir_hola_mundo()

# 2. Hola personalizado.
print("--- Ejercicio 2: Hola personalizado ---")

def saludar_usuario(nombre):
  print(f"¡Hola {nombre}!")

nombre_input = input("Dime tu nombre: ").strip()
if nombre_input.replace(" ","").isalpha():
  saludar_usuario(nombre_input.capitalize())
else:
  print("Debe ingresar un nombre correcto")

# 3. Información personal.
print("--- Ejercicio 3: Información personal ---")

def informacion_personal(nombre, apellido, edad, residencia):
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

while True:
  nombre = input("Dime tu nombre: ").strip()
  apellido = input("Dime tu apellido: ").strip()
  edad = input("Dime tu edad: ").strip()
  residencia = input("Dime tu país de residencia: ").strip()
  if nombre.isalpha() and apellido.isalpha() and edad.isdigit() and residencia.isalpha():
    informacion_personal(nombre.capitalize(),apellido.capitalize(),edad,residencia.capitalize())
    break
  else:
    print("Ingrese los datos correctamente...")

# 4. Área y perímetro del círculo con funciones.
print("--- Ejercicio 4: Área y perímetro del círculo ---")

def calcular_area_circulo(radio):
  return 3.1416 * (radio ** 2)

def calcular_perimetro_circulo(radio):
  return 2 * radio * 3.1416

radio_input = input_float("Ingrese el radio: ")
print(f"El área del círculo es: {calcular_area_circulo(radio_input):.2f}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio_input):.2f}")

# 5. Función segundos a horas.
print("--- Ejercicio 5: Segundos a horas ---")

def segundos_a_horas(segundos):
  return segundos / 3600

print(f"La cantidad de horas equivalentes es: {segundos_a_horas(input_entero('Dime la cantidad de segundos: ')):.2f} horas")

# 6. Tabla de multiplicar de un número.
print("--- Ejercicio 6: Tabla de multiplicar ---")

def tabla_multiplicar(numero):
  print(f"Tabla de multiplicar del {numero}")
  for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar(input_entero("Ingresar un número para imprimir su tabla de multiplicar: "))

# 7. Operaciones básicas con dos números enteros.
print("--- Ejercicio 7: Operaciones básicas ---")

def operaciones_basicas(a, b):
  suma = a + b
  resta = a - b
  multiplicacion = a * b
  if b != 0:
    division = a / b
  else:
    division = "No se puede dividir por cero"
  return suma,resta,multiplicacion,division

resultado = operaciones_basicas(input_float("Ingrese el primer número para realizar las operaciones básicas: "),input_float("Ingrese el segundo número: "))
print(f"Resultado Suma: {resultado[0]}")
print(f"Resultado Resta: {resultado[1]}")
print(f"Resultado Multiplicación: {resultado[2]}")
print(f"Resultado División: {resultado[3]}")

# 8. Calculadora de Índice de Masa Corporal.
print("--- Ejercicio 8: Cálculo de IMC ---")

def calcular_imc(peso, altura):
  if altura > 0 and peso > 0:
    imc = peso / altura ** 2
    return imc
  else:
    return "Eror ingrese una altura y peso mayor a cero!"

print(f"El IMC es: {calcular_imc(input_float('Ingrese su peso para calcular el IMC: '),input_float('Ingrese su altura: ')):.2f}")

# 9. Función de Celsius a Fahrenheit.
print("--- Ejercicio 9: Celsius a Fahrenheit ---")

def celsius_a_fahrenheit(celsius):
  return (celsius * 1.8) + 32

print(f"Temperatura en °F: {celsius_a_fahrenheit(input_float('Ingrese la temperatura en °C : '))}")

# 10. Calcular promedio de 3 números.
print("--- Ejercicio 10: Promedio de 3 números ---")

def calcular_promedio(a, b, c):
  return (a + b + c ) / 3

num1 = input_float("Ingrese el primer número: ")
num2 = input_float("Ingrese el segundo número: ")
num3 = input_float("Ingrese el tercer número: ")
print(f"El promedio de los números {num1}, {num2}, {num3} es: {calcular_promedio(num1,num2,num3):.2f}")