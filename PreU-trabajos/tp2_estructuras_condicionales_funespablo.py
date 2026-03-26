# Ejercicio 1 Mayor de edad
print("Comienza el ejercicio 1")
edad = int(input("Dime tu edad: "))
if edad >= 18:
    print("Es mayor de edad")
# Ejercicio 2 Aprobado / Desaprobado
print("Comienza el ejercicio 2")
nota = float(input("Dime la nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
# Ejercicio 3 Solo números pares
print("Comienza el ejercicio 3")
numero = int(input("Dime un número par: "))
if numero%2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par") #En este caso se debería usar una estructura repetitiva para volver a ejecutar el programa desde el principio
# Ejercicio 4 Edad por categorias
print("Comienza el ejercicio 4")
edad2 = int(input("Dime tu edad: "))
if edad2 < 12:
    print("Eres niño/a")
elif edad2 >= 12 and edad2 < 18:
    print("Eres adolescente")
elif edad2 >= 18 and edad2 < 30:
    print("Eres adulto/a joven")
elif edad2 >= 30:
    print("Eres adulto/a")
# Ejercicio 5 Contraseña de 8-14 caracteres
print("Comienza el ejercicio 5")
contraseña = len(input("Dime una de contraseña de 8 a 10 caracteres: "))
if contraseña >= 8 and contraseña <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# Ejercicio 6 Sesgo positivo/negativo o sin sesgo
print("Comienza el ejercicio 6")
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"""
    Media: {media}
    Mediana: {mediana}
    Moda: {moda}
    """)
if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana == moda:
    print("No hay sesgo")
else:
    print("El resultado no está dentro de los valores")
# Ejercicio 7 Signo de exclamación
print("Comienza el ejercicio 7")
frase = input("Dime una frase o palabra: ")
ultima_letra = frase[-1].lower()
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    frase_nueva = frase + "!"
    print(frase_nueva)
else:
    print(frase)
# Ejercicio 8 Opciones condicionales
print("Comienza el ejercicio 8")
nombre = input("Ingrese su nombre: ")
opcion = int(input("""
    Ingrese una opción:
    1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
    """))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
# Ejercicio 9 Magnitud de terremoto
print("Comienza el ejercicio 9")
magnitud = float(input("Ingrese la magnitud de terremoto: "))
if magnitud < 3:
    print('"Muy leve" (imperceptible)')
elif magnitud >= 3 and magnitud < 4:
    print('"Leve" (ligeramente perceptible)')
elif magnitud >= 4 and magnitud < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños)')
elif magnitud >= 5 and magnitud < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles)')
elif magnitud >= 6 and magnitud < 7:
    print('"Muy Fuerte" (puede causar daños significativos)')
else:
    print('"Extremo" (puede causar graves daños a gran escala)')
# Ejercicio 10 Estaciones del año
print("Comienza el ejercicio 10")
hemisferio = input("Dime en cuál hemisferio se encuentra (N/S): ")
mes = int(input("Dime qué mes del año es (en número): "))
dia = int(input("Dime qué día es: "))
if (mes < 1) or (mes > 12) or (dia < 1) or (dia > 31):
    print("Ingrese una fecha correcta")
elif hemisferio.lower() == "n":
    if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or mes == 1 or mes == 2:
        print("Te encuentras en invierno")
    elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or mes == 4 or mes == 5:
        print("Te encuentras en primavera")
    elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or mes == 7 or mes == 8:
        print("Te encuentras en verano")
    elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or mes == 10 or mes == 11:
        print("Te encuentras en otoño")
elif hemisferio.lower() == "s":
    if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or mes == 1 or mes == 2:
        print("Te encuentras en verano")
    elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or mes == 4 or mes == 5:
        print("Te encuentras en otoño")
    elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or mes == 7 or mes == 8:
        print("Te encuentras en invierno")
    elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or mes == 10 or mes == 11:
        print("Te encuentras en primavera")
else:
    print("ingrese un hemisferio correcto...")