import csv

def menu():
    print('''
    MENÚ PRINCIPAL
    1. Agregar libro
    2. Mostrar libros
    3. Buscar libro
    4. Modificar libro
    5. Eliminar libro
    6. Estadísticas
    7. Salir
        ''')

def cargar_archivo():
    lista = []
    try:
        with open('biblioteca.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                lista.append({
                    'titulo': fila['titulo'],
                    'autor': fila['autor'],
                    'anio': int(fila['anio']),
                    'stock': fila['stock']
                })
        print('Archivo cargado.')
        
    except FileNotFoundError:
        print('El archivo no existe')
    except PermissionError:
        print('No tenes permiso de lectura.')
    except ValueError:
        print('El año no es un numero.')
        
    return lista


def input_int(mensaje,mensaje2=None):
    while True:
        try:
            opcion = int(input(mensaje))
            return opcion
        except ValueError:
            print(mensaje2 if mensaje2 != None else 'Error' )

def opcion1():
    pass