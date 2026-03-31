# 13) Dada la siguiente lista de puntajes de un videojuego:
# puntajes = [450, 1200, 875, 990, 300, 1500, 640]
# ● Mostrar el puntaje más alto y el más bajo.
# ● Mostrar la lista ordenada de mayor a menor (ranking).
# ● Indicar en qué posición del ranking se encuentra el puntaje 990.

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

puntajes_ordenado = sorted(puntajes)

print("El ranking de puntajes es: ")
for num in puntajes_ordenado:
    print(num,end=" | ")
    
print(f"\nEl puntaje mas bajo es: {puntajes_ordenado[0]}")
print(f"El puntaje mas alto es: {puntajes_ordenado[-1]}")
print(f"La posición del puntaje 990 es la posición: {puntajes_ordenado.index(990) + 1}")
