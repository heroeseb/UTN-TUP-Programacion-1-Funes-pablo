# 12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
# ● Mostrar la lista original.
# ● Mostrar la lista ordenada de menor a mayor.
# ● Mostrar la lista ordenada de mayor a menor.
# ● Investigar el uso de sorted() y del parámetro reverse.

numeros = []
cantidad_numeros = 8
for i in range (cantidad_numeros):
    while True:
        num = input(f"Ingrese el numero {i+1}: ")
        if num.isdigit():
            num_int = int(num)
            numeros.append(num_int)
            break
        else:
            print("Ingrese un numero correcto...")
lista_ordenada_creciente,lista_ordenada_decreciente = sorted(numeros),sorted(numeros,reverse=True)
print("Lista de numeros sin ordenar:")
for num in numeros:
    print(num,end=" | ")
print("\nLista de numeros ordenada de menor a mayor:")
for num in lista_ordenada_creciente:
    print(num,end=" | ")
print("\nLista de numeros ordenada de mayor a menor:")
for num in lista_ordenada_decreciente:
    print(num,end=" | ")
