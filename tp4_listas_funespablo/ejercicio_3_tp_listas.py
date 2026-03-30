
# Ejercicio 3 Lista pares e impares
lista = []
pares = []
impares = []
import random
for i in range(15):
    numero = random.randint(1,100)
    lista.append(numero)
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Los números de la lista ({len(lista)} números) son: ")
for num in lista:
    print(num,end=" ")
print(f"\nLos números pares son {len(pares)}: ")
for num in pares:
    print(num,end=" ")
print(f"\nLos números impares son {len(impares)}: ")
for num in impares:
    print(num,end=" ")