
# Ejercicio 8 Notas de estudiantes
notas = [
    ["Ana", 8.5, 7.0, 9.0],
    ["Luis", 6.0, 8.0, 7.5],
    ["María", 9.0, 9.5, 8.0],
    ["Carlos", 7.0, 6.5, 8.5],
    ["Sofía", 8.0, 7.5, 9.0]
]
suma_materi1 = 0
suma_materi2 = 0
suma_materi3 = 0
for nombre, nota1, nota2, nota3 in notas:
    promedio = (nota1 + nota2 + nota3) / 3
    suma_materi1 += nota1
    suma_materi2 += nota2
    suma_materi3 += nota3
    print(f"{nombre} : materia 1 : {nota1}, materia 2 : {nota2}, materia 3 : {nota3} , su promedio de notas es: {promedio:.2f}")
print(f"""El promedio de las materias son: 
    materia 1 : {suma_materi1/len(notas):.2f}
    materia 2 : {suma_materi2/len(notas):.2f} 
    materia 3 : {suma_materi3/len(notas):.2f}
    """)