
########################### CARGAR DATOS DE UN CSV####################
import csv
csv_productos = 'productos.csv'
productos = []
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
print(productos)
##########################################################################

###################INPUT TIPO STRING######################################
def input_str(mensaje,mensaje_2=None):
    try:
        input_salid = input(mensaje)
        if not input_salid.isalpha():
            raise TypeError
        return input_salid
    except TypeError:
        print(mensaje_2 if mensaje_2 else 'Error de tipo')
#############################################################################
#######################INPUT TIPO INTERGER O FLOAT###########################
def input_int_or_float(tipo,mensaje,mensaje_2=None):
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
###############################################################################
#############GENERAR ID EN UNA BIBLIOTECA######################################
def generador_id(lista):
    if len(lista) == 0:
        return 1
    else:
        id_nuevo = lista[-1]['id'] + 1
        return id_nuevo
##############################################################################
###################AGREGAR PRODUCTO###########################################
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
#############################################################################################
####################GUARDAR DATOS###########################################################
Fieldnames = []
def guardar_datos(lista):
    with open(csv_productos,'w',newline='',encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo,fieldnames=Fieldnames)
        writer.writeheader()
        writer.writerows(lista)
        print('Se guardaron correctamente los datos')
##############################################################################################
################### MOSTRAR PRODUCTOS ########################################################
def mostrar_productos(lista):
    for producto in lista:
        print('-'*50)
        for k,v in producto.items():
            print(f'{k.capitalize()} : {v}')
#############################################################################################
########################## MOSTRAR PRODUCTO INDIVIDUAL #######################################
def mostrar_producto_individual(diccionario):
    print('-'*50)
    for k,v in diccionario.items():
        print(f'{k.capitalize()} : {v}')
    print('-'*50)
############################################################################################
####################### BUSCAR PRODUCTO POR ID O NOMBRE ###################################
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
##########################################################################################################
####################   MODIFICAR PRODUCTO ################################################################
def modificacion(diccionario):
    diccionario_copia = diccionario.copy()
    nombre = input_str('Ingrese el nombre del producto(si no deseas modificarlo ingresa no): ','Ingrese un nombre valido')
    if nombre != 'No':
        diccionario_copia['nombre'] = nombre
    categoria = input_str('Ingrese la categoria del producto(si no deseas modificarlo ingresa no): ','Ingrese una categoria valida')
    if categoria != 'No':
        diccionario_copia['categoria'] = categoria
    precio = input_int_or_float('float','Ingrese el precio del producto(si no desea modificar ingrese 0): ')
    while not precio >= 0:
        print('El un numero mayor o igual a cero!')
        precio = input_int_or_float('float','Ingrese el precio del producto(si no desea modificar ingrese 0): ')
    if precio != 0:
        diccionario_copia['precio'] = precio
    stock = input_int_or_float('int','Ingrese el Stock(si no desea modificar ingrese -1): ')
    while not stock >= -1:
        print('Ingrese un numero mayor o igual a -1!')
        stock = input_int_or_float('int','Ingrese el Stock(si no desea modificar ingrese -1): ')
    if stock != -1:
        diccionario_copia['stock'] = stock
    return diccionario_copia

def modificar_producto(lista):
    copia_lista = lista.copy()
    print('Ingrese si desea buscar el producto a modificar por:')
    print('1. ID')
    print('2. Nombre')
    opcion = input_int_or_float('int','Ingrese una opción: ','Solo se pueden ingresar numeros!')
    match opcion:
        case 1:
            id_buscado = input_int_or_float('int','Ingrese el ID a buscar: ','Solo se permiten numeros')
            encontrado = False
            for i in range(len(copia_lista)):
                if copia_lista[i]['id'] == id_buscado:
                    print('-'*50)
                    print('El producto sin modificar: ')
                    mostrar_producto_individual(copia_lista[i])
                    encontrado = True
                    copia_lista[i] = modificacion(copia_lista[i])
                    print('Producto modificado con exito!')
                    return copia_lista
            if not encontrado:
                print('No se encontro el producto con ese ID!')
            return copia_lista
        case 2:
            nombre_buscado = input_str('Ingrese el nombre del articulo a buscar: ','Solo se permiten letras')
            encontrado = False
            for i in range(len(copia_lista)):
                if copia_lista[i]['nombre'].capitalize() == nombre_buscado:
                    print('-'*50)
                    print('El producto sin modificar: ')
                    mostrar_producto_individual(copia_lista[i])
                    encontrado = True
                    copia_lista[i] = modificacion(copia_lista[i])
                    print('Producto modificado con exito!')
                    return copia_lista
            if not encontrado:
                print('No se encontro el producto con ese nombre!')
            return copia_lista
        case _:
            print('Ingrese una opcion correcta (1 o 2)!')
################################################################################################################
######################### ELIMINAR PRODUCTO #################################################################
def eliminar_producto(lista):
    copia_lista = lista.copy()
    id_buscado = input_int_or_float('int','Ingrese el ID a buscar: ','Solo se permiten numeros')
    encontrado = False
    for i in range(len(copia_lista)):
        if copia_lista[i]['id'] == id_buscado:
            print('-'*50)
            print('El producto es: ')
            mostrar_producto_individual(copia_lista[i])
            encontrado = True
            decision = input_str('Confirma la eliminación del producto?(si o no): ')
            if not decision == 'Si':
                print('Cancelaste la eliminación!')
            else:
                copia_lista.pop(i)
                print('Producto eliminado con exito!')
            return copia_lista
    if not encontrado:
        print('No se encontro el producto con ese ID!')
    return copia_lista
#################################################################################################
#######################     MOSTRAR ESTADISTICAS    ###############################################
def mostrar_estadisticas(lista):
    total_productos = 0
    producto_mas_caro = 0
    stock_total = 0
    lista_precios_todos = sum([e['precio'] for e in lista])
    for elemento in lista:
        total_productos += 1
        if elemento['precio'] > producto_mas_caro:
            producto_mas_caro = elemento['precio']
        stock_total += elemento['stock']
    print(f'La cantidad total de productos es: {total_productos}')
    print(f'El producto más caro es: {producto_mas_caro}')
    print(f'El promedio de precios es: {lista_precios_todos/len(lista):.2f}')
    print(f'El stock total es: {stock_total}')
#####################################################################################################