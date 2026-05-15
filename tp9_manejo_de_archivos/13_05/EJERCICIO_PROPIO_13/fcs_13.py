# Parte 3 — Ejercicio Integrador Completo
# Sistema de Gestión de Productos

# Objetivo
# Desarrollar un sistema ABM completo usando:
# • funciones 
# • listas de diccionarios 
# • manejo de archivos CSV
# • csv.DictReader 
# • csv.DictWriter 
# • validaciones 
# • búsqueda 
# • persistencia automática 
# Requisitos del sistema
# Cada producto tendrá:
# • ID 
# • nombre 
# • categoría 
# • precio 
# • stock 
# Ejemplo:
# {
#  "id": "1",
#  "nombre": "Mouse",
#  "categoria": "Periférico",
#  "precio": 15000,
#  "stock": 10
# }

# Funcionalidades obligatorias

# 1. Cargar datos automáticamente desde CSV
# Al iniciar el programa:
# • leer el archivo productos.csv 
# • cargar los datos en una lista de diccionarios 
# Si el archivo no existe:
# • comenzar con lista vacía 
import csv
csv_productos = 'productos.csv'
productos = []
Fieldnames = ['id','nombre','categoria','precio','stock']
def cargar_datos(product):
    productos = []
    try:
        with open(product,'r',encoding='utf-8',newline='') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                try:
                    fila['id'] = int(fila['id'])
                    fila['precio'] = float(fila['precio'])
                    fila['stock'] = int(fila['stock'])
                    productos.append(fila)
                except (ValueError,KeyError,TypeError):
                    print('Se ignoro una linea invalida del CSV')
    except FileNotFoundError:
        print("El archivo no existe. Se creará una lista vacía.")
    except PermissionError:
        print("Error... No tenes permiso de lectura en este archivo.")
    return productos
productos = cargar_datos(csv_productos)
# 2. Alta de productos
# Permitir:
# • ingresar datos 
# • validar: 
# o precio > 0 
# o stock >= 0 
# o ID único
# Al agregar:
# • guardar automáticamente en CSV 

def input_str(mensaje,mensaje_2=None):
    while True:
        try:
            input_salid = input(mensaje).strip()
            if not input_salid.replace(' ','').isalpha():
                raise TypeError
            return input_salid.capitalize()
        except TypeError:
            print(mensaje_2 if mensaje_2 else 'Error de tipo')

def input_int_or_float(tipo,mensaje,mensaje_2=None):
    while True:
        try:
            match tipo:
                case 'int':
                    input_salid = int(input(mensaje))
                    return input_salid
                case 'float':
                    input_salid = float(input(mensaje))
                    return input_salid
        except ValueError:
            print(mensaje_2 if mensaje_2 else 'Error de valor')

def generador_id(lista):
    if len(lista) == 0:
        return 1
    else:
        id_nuevo = lista[-1]['id'] + 1
        return id_nuevo

def agregar_producto(lista):
    nombre = input_str('Ingrese el nombre del producto: ','Ingrese un nombre valido')
    categoria = input_str('Ingrese la categoria del producto: ','Ingrese una categoria valida')
    precio = input_int_or_float('float','Ingrese el precio del producto: ')
    while not precio > 0:
        print('El precio debe ser mayor a cero!')
        precio = input_int_or_float('float','Ingrese el precio del producto: ')
    stock = input_int_or_float('int','Ingrese el Stock: ')
    while not stock >= 0:
        print('El stock debe ser mayor o igual a cero!')
        stock = input_int_or_float('int','Ingrese el Stock: ')
    if not(nombre and categoria and precio and stock):
        print ('Faltan datos/se cargaron incorrectamente los datos!...')
    else:
        diccionario = {'id' : generador_id(lista),
                        'nombre': nombre,
                        'categoria': categoria,
                        'precio': precio,
                        'stock': stock}
        print('Se agrego correctamente el producto!')
        return diccionario

def guardar_datos(lista):
    with open(csv_productos,'w',newline='',encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo,fieldnames=Fieldnames)
        writer.writeheader()
        writer.writerows(lista)
        print('Se guardaron correctamente los datos')

'''producto = agregar_producto(productos)
productos.append(producto)
guardar_datos(productos)
print(productos)
'''
# 3. Mostrar productos
# Mostrar todos los productos de forma prolija.
def mostrar_productos(lista):
    for producto in lista:
        print('-'*50)
        for k,v in producto.items():
            print(f'{k.capitalize()} : {v}')
mostrar_productos(productos)

def mostrar_producto_individual(diccionario):
    print('-'*50)
    for k,v in diccionario.items():
        print(f'{k.capitalize()} : {v}')
    print('-'*50)
# 4. Buscar producto
# Buscar por:
# • ID 
# • nombre 
def buscar_producto(lista):
    print('Ingrese si desea buscar por:')
    print('1. ID')
    print('2. Nombre')
    opcion = input_int_or_float('int','Ingrese una opción: ','Solo se pueden ingresar numeros!')
    match opcion:
        case 1:
            id_buscado = input_int_or_float('int','Ingrese el ID a buscar: ','Solo se permiten numeros')
            encontrado = False
            for linea in lista:
                if linea['id'] == id_buscado:
                    mostrar_producto_individual(linea)
                    encontrado = True
            if not encontrado:
                print('No se encontro el producto con ese ID!')
        case 2:
            nombre_buscado = input_str('Ingrese el nombre del articulo a buscar: ','Solo se permiten letras')
            encontrado = False
            for linea in lista:
                if linea['nombre'].capitalize() == nombre_buscado:
                    mostrar_producto_individual(linea)
                    encontrado = True
            if not encontrado:
                print('No se encontro el producto con ese nombre!')
        case _:
            print('Ingrese una opcion correcta (1 o 2)!')
buscar_producto(productos)
#
# 5. Modificar producto
# Permitir modificar:
# • nombre 
# • categoría 
# • precio 
# • stock 
# Luego:
# • guardar automáticamente 
# 6. Eliminar producto
# Eliminar por ID.
# Confirmar antes de borrar.
# Luego:
# • guardar automáticamente 
# 7. Estadísticas
# Mostrar:
# • cantidad total de productos 
# • producto más caro 
# • promedio de precios 
# • stock total 
# Restricciones importantes
# NO debe existir:
# • opción “Guardar” 
# • opción “Cargar”
# El guardado debe ser AUTOMÁTICO:
# • después de alta 
# • después de modificación 
# • después de eliminación 
# Menú esperado
# 1. Agregar producto
# 2. Mostrar productos
# 3. Buscar producto
# 4. Modificar producto
# 5. Eliminar producto
# 6. Estadísticas
# 7. Salir
# Recomendaciones técnicas
# Archivo CSV
# Nombre sugerido:
# productos.csv
# Estructura recomendada
# Funciones sugeridas:
# cargar_datos()
# guardar_datos()
# agregar_producto()
# mostrar_productos()
# buscar_producto()
# modificar_producto()
# eliminar_producto()
# mostrar_estadisticas()
# menu()

# # EXTRA
# # Agregar:
# # • ordenar productos por precio 
# # • filtrar por categoría 
# # • evitar IDs duplicados 
# # • validar errores con try/except 
# # • fecha de creación 
# # • búsqueda parcial 
# # • exportar productos sin stock