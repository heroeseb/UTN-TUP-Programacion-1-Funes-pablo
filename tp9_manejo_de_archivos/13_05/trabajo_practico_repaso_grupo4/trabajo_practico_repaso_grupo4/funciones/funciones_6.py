def mostrar_estudiantes(estudiantes):
    dic_estudiantes = dict(estudiantes)
    print("Estudiantes:")
    for i in dic_estudiantes.keys():
        print(f"-{i}")

def nota_más_alta(estudiantes):
    i, k = max(estudiantes, key=lambda x: x[1]) # aca lo que hago es buscar la clave y la llave, en base a la llave más alta lo imprimo todo gracias al lambda
    # "lambda x: x[1]" toma la tupla, y me da su segundo elemento
    print(f"La nota más alta es: {k}, perteneciente a {i}.")

def promedio_general(estudiantes):
    dic_estudiantes = dict(estudiantes)
    promedio = sum(dic_estudiantes.values()) / len(dic_estudiantes)
    print(f"El promedio general es: {promedio}.")