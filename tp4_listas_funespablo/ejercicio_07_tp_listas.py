
# Ejercicio 7 Matriz temperatura Min y Max
temperaturas = [
    [11, 25],  # Lunes
    [13, 20],  # Martes
    [11, 21],  # Miércoles
    [13, 23],  # Jueves
    [16, 27],  # Viernes
    [16, 26],  # Sábado
    [8, 15]   # Domingo
]
sum_min = 0
sum_max = 0
mayor_amplitud = 0
mayor_amplitud_dia = 0
contador = 0
for minimo,maximo in temperaturas:
    print(f"Min {minimo}° - Max {maximo}°")
    contador += 1
    sum_max += maximo
    sum_min += minimo
    amplitud = maximo - minimo
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        mayor_amplitud_dia = contador
print(f"El promedio de las temperaturas máximas es: {(sum_max/7):.0f}°")
print(f"El promedio de las temperaturas mínimas es: {(sum_min/7):.0f}°")
print(f"El día que se registró la mayor amplitud térmica fue: Min {temperaturas[mayor_amplitud_dia-1][0]} ° - Max {temperaturas[mayor_amplitud_dia-1][1]}°")