# Ejercicio 1 "Hola mundo"
print("Hola Mundo!")
# Ejercicio 2 Saludo
print("Comienza el ejercicio 2")
nombre = input("Dime tu nombre: ")
print(f"Hola {nombre}!")
# Ejercicio 3 Presentación
print("Comienza el ejercicio 3")
nombre = input("Dime tu nombre: ")
apellido = input("Dime tu apellido: ")
edad = input("Dime tu edad: ")
residencia = input("Dime tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
# Ejercicio 4 Area y perímetro
print("Comienza el ejercicio 4")
radio = float(input("Dime el radio del círculo"))
area = 3.1416 * (radio ** 2)
perimetro = 3.1416 * radio * 2
print(f"El área del círculo es: {area}, y el perímetro es: {perimetro}")
# Ejercicio 5 De segundos a Horas
print("Comienza el ejercicio 5")
segundos = int(input("Dime la cantidad de segundos a convertir: "))
horas = segundos / 3600
print(f"{segundos} segundos equivale a: {horas} horas")
# Ejercicio 6 Tabla de multiplicar
print("Comienza el ejercicio 6")
numero = int(input("Dime un numero para mostrar su tabla de multiplicar: "))
print(f"""
        La tabla de multiplicar de {numero} es:
        {numero} x 1 = {numero * 1}
        {numero} x 2 = {numero * 2}
        {numero} x 3 = {numero * 3}
        {numero} x 4 = {numero * 4}
        {numero} x 5 = {numero * 5}
        {numero} x 6 = {numero * 6}
        {numero} x 7 = {numero * 7}
        {numero} x 8 = {numero * 8}
        {numero} x 9 = {numero * 9}
        {numero} x 10 = {numero * 10}
        """)
# Ejercicio 7 Suma,resta,multiplicación y división
print("Comienza el ejercicio 7")
numero1 = int(input("Dime el primer numero(distinto de cero): "))
numero2 = int(input("Dime el segundo numero(distinto de cero): "))
print(f"""
        Los resultados son:
        {numero1} + {numero2} = {numero1 + numero2}
        {numero1} / {numero2} = {numero1 / numero2}
        {numero1} * {numero2} = {numero1 * numero2}
        {numero1} - {numero2} = {numero1 - numero2}
        """)
# Ejercicio 8 IMC
print("Comienza el ejercicio 8")
altura = float(input("Dime la altura en metros: "))
peso = float(input("Dime el peso en kg: "))
imc = peso / (altura**2)
print(f"El indice de masa corporal es: {imc}")
# Ejercicio 9 Conversor de temperatura
print("Comienza el ejercicio 9")
temperatura = float(input("Dime la temperatura en grados Celcius: "))
fahrenheit = (9 / 5) * temperatura + 32
print(f"{temperatura}°C son {fahrenheit}°F")
# Ejercicio 10 Promedio
print("Comienza el ejercicio 10")
primero = float(input("Dime el primer numero"))
segundo = float(input("Dime el segundo numero"))
tercero = float(input("Dime el tercer numero"))
promedio = (primero + segundo + tercero) / 3
print(f"El promedio de los numeros es: {promedio}")