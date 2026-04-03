# 13) Dada la siguiente lista de puntajes de un videojuego:
# puntajes = [450, 1200, 875, 990, 300, 1500, 640]
# ● Mostrar el puntaje más alto y el más bajo.
# ● Mostrar la lista ordenada de mayor a menor (ranking).
# ● Indicar en qué posición del ranking se encuentra el puntaje 990.

puntajes = [450, 1200, 875, 990, 300, 1500, 640]
puntajes_ordenado = sorted(puntajes, reverse=True)
print("El ranking de puntajes es: ")
for num in puntajes_ordenado:
    print(num,end=" | ")
print(f"\nEl puntaje más bajo es: {puntajes_ordenado[-1]}")
print(f"El puntaje más alto es: {puntajes_ordenado[0]}")
print(f"El puntaje 990 está en la posición: {puntajes_ordenado.index(990) + 1}")
