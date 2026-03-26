# Ejercicio 1 Numeros del 1 al 100
print("Comienza el ejercicio 1")
for i in range(1,101):
    print(i)
# Ejercicio 2 Cantidad de dígitos
print("Comienza el ejercicio 2")
numero = input("Dime un número entero: ")
cont_digitos = 0
for i in numero:
    cont_digitos += 1 #Esto suponiendo que es un número positivo, si no habria que hacer otro procedimiento para no contar el "-"
print(f"El número tiene {cont_digitos} dígitos")
# Ejercicio 3 Suma de numeros
print("Comienza el ejercicio 3")
num1 = int(input("Dime el primer número entero: "))
num2 = int(input("Dime el segundo número entero: "))
if num1 > num2:
    numx = num1
    num1 = num2
    num2 = numx
sumatoria = 0
for i in range(num1,num2):
    if i == num1 or i == num2:
        continue
    else:
        sumatoria += i
print(f"La suma de los números es: {sumatoria}")
# Ejercicio 4 Suma de varios números
print("Comienza el ejercicio 4")
cierre = True
suma = 0
while cierre:
    numer = int(input("Dime un número para sumar (ingresa 0 para terminar): "))
    if numer == 0:
        cierre = False
    else:
        suma += numer
print(f"La suma de todos los números es: {suma}")
# Ejercicio 5 Juego adivinar
print("Comienza el ejercicio 5")
import random
num_aleatorio = random.randint(0,9)
intentos = 0
acierto = True
while acierto:
    num_adivinar = int(input("Dime un número del 0 al 9: "))
    if 9 >= num_adivinar >= 0:
        intentos += 1
        if num_adivinar == num_aleatorio:
            print(f"Adivinaste el número!! en {intentos} intentos")
            acierto = False
        elif num_adivinar < num_aleatorio:
            print("El número es más alto... vuelve a intentarlo")
        else:
            print("El número es más bajo... vuelve a intentarlo")
    else:
        print("Ingrese un número correcto...")
# Ejercicio 6 Pares de 0 a 100 decreciente
print("Comienza el ejercicio 6")
for i in range(100,-1,-1):
    if i%2 == 0:
        print(i)
    else:
        continue
# Ejercicio 7 Suma de números positivos
print("Comienza el ejercicio 7")
suma_positiva = 0
while True:
    numero_suma = int(input("Dime un número positivo: "))
    if numero_suma > 0:
        for i in range(numero_suma+1):
            suma_positiva += i
        print(f"La suma de todos los números es {suma_positiva}")
        break
    else:
        print("Ingrese un número positivo...")
# Ejercicio 8 Pares/Impares-Positivos/Negativos
print("Comienza el ejercicio 8")
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(100):
    numeroo = int(input("Dime un número: "))
    if numeroo >= 0:
        positivos += 1
    else:
        negativos += 1
    if numeroo%2 == 0:
        pares += 1
    else:
        impares += 1
print(f"""
    Cantidad de números positivos: {positivos}
    Cantidad de números negativos: {negativos}
    Cantidad de números pares: {pares}
    Cantidad de números impares: {impares}
    """)
# Ejercicio 9 Media de 100 números
print("Comienza el ejercicio 9")
suma9 = 0
repeticiones = 100
for i in range(repeticiones):
    numeros9 = int(input("Dime un número: "))
    suma9 += numeros9
print(f"La media de los números es: {suma9/repeticiones}")
# Ejercicio 10 Invertir un número
print("Comienza el ejercicio 10")
numero_10 = input("Dime el número que quieres invertir el orden de dígitos: ")
numero_inv = ""
for i in range(len(numero_10)-1, -1, -1):
    numero_inv += numero_10[i]
print(f"El número invertido es: {numero_inv}")