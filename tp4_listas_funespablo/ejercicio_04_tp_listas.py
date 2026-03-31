
# Ejercicio 4 Valores repetidos
datos = [1,3,5,3,7,1,9,5,3]
print("La lista completa es: ")
for dato in datos:
    print(dato,end=" ")
lista_nueva = []
for dat in datos:
    if dat in lista_nueva:
        continue
    else:
        lista_nueva.append(dat)
print(f"\nLa lista sin repetir números es: ")
for numero_nuevo in lista_nueva:
    print(numero_nuevo,end=" ")