import csv

def mostrar_menu():
    print('''1. Registrar estudiante
2. Mostrar estudiantes
3. Guardar archivo
4. Estadísticas
5. Salir''')
    
def cargar_archivo():
    lista = []
    try:
        with open('asistencias.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                lista.append({
                    'nombre': fila['nombre'],
                    'edad': int(fila['edad']),
                    'presente': fila['presente']
                })
        print('Archivo cargado.')
        
    except FileNotFoundError:
        print('El archivo no existe')
    except PermissionError:
        print('No tenes permiso de lectura.')
    except ValueError:
        print('La edad no es un numero.')
        
    return lista

def agregar_estudiante(lista):
    try:
        nombre = input('Ingrese el nombre del estudiante: ').title()
        edad = int(input('Ingrese la edad del estudiante: '))
        presente = input('Ingrese si / no para la asistencia del estudiante: ').lower()
        
        nvo_estudiante = {
            'nombre': nombre,
            'edad': edad,
            'presente': presente
        }
        
        lista.append(nvo_estudiante)
        print('Estudiante agregado')
    except ValueError:
        print('Debe ingresar un número entero.')
    
    return lista

def mostrar_estudiantes(lista):
    for est in lista:
        print(f'Nombre: {est['nombre']}')
        print(f'Edad: {est['edad']}')
        print(f'Presente: {est['presente']}')
        print()
        
def guardar_archivo(lista):
    try:
        with open('asistencias.csv', 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=['nombre', 'edad', 'presente'])
            
            writer.writeheader()
            writer.writerows(lista)
            
        print('Archivo guardado.')
    except FileNotFoundError:
        print('El archivo no existe.')
    except PermissionError:
        print('No tiene permiso de escritura.')
    
def estadisticas(lista):
    try:
        print(f'Total de estudiantes: {len(lista)}')
        
        presentes = 0
        suma_edad = 0
        
        for est in lista:
            suma_edad += est['edad']
            
            if(est['presente'] == 'si'):
                presentes += 1
        
        print(f'El total de estudiantes presentes es: {presentes}')
        print(f'El total de estudiantes ausentes es: {len(lista) - presentes}')
        print(f'El promedio de edades de la lista es: {(suma_edad / len(lista)):.2f}')
    except ZeroDivisionError:
        print('No hay estudiantes en la lista.')