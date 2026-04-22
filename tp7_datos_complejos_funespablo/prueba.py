def input_entero_convert(mensaje,mensaje2):
    while True:
        opcion = input(mensaje).strip()
        if opcion.replace(".","",1).isdigit():
            if "." in opcion:
                return float(opcion)
            else:
                return int(opcion)
        else:
            print(mensaje2)
def input_string(mensaje,mensaje2):
    while True:
        opcion = input(mensaje).strip()
        if opcion.replace(" ","").isalpha():
            return opcion.capitalize()
        else:
            print(mensaje2)

print('-'*50)
print('Ejercicio 7')

print('Lista de asistencia original: ')
asistencias = [
    "Ana", "Luis", "Marta", "Ana", "Carlos",
    "Luis", "Ana", "Marta", "Pedro", "Luis",
    "Sofia", "Carlos", "Ana", "Pedro", "Sofia",
    "Marta", "Luis", "Ana"
]
print(*asistencias,sep=' , ')

set_asistencia = set(asistencias)
print('Empleados que asistieron al menos una vez: ')
print(*set_asistencia,sep=' , ')

for empleado in set_asistencia:
    print(f'Empleado {empleado} asistió: {asistencias.count(empleado)} veces')