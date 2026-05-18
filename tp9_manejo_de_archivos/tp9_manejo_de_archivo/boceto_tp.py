
# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
p1 = "Lapicera,120.5,30\n"
p2 = "Cuaderno,450.0,15\n"
p3 = "Goma,80.25,50\n"

def crear_archivo_txt(l1,l2,l3):
    '''
    .write() solo puede recibir string de otra forma tira un error de tipo
    '''
    try:
        with open('productos.txt','w',encoding='utf-8') as archivo:
            archivo.write(l1)
            archivo.write(l2)
            archivo.write(l3)
    except TypeError:
        print('Solo se puede ingresar datos del tipo String!')

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30
def leer_mostrar_productos():
    try:
        with open('productos.txt','r',encoding='utf-8') as archivo:
            for linea in archivo:
                try:
                    datos = linea.strip().split(',')
                    nombre = datos[0]
                    precio = datos[1]
                    cantidad = datos[2]
                    print(f'Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}')
                except IndexError:
                    print('Se salteo una linea porque faltan datos!')
    except FileNotFoundError:
        print('El archivo no existe!')
    except PermissionError:
        print('No se tiene permisos para acceder al archivo!')
# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

leer_mostrar_productos()

def crear_linea():
    producto_nombre = input('Ingrese el nombre del nuevo producto: ')
    producto_precio = input('Ingrese el precio del nuevo producto: ')
    producto_cantidad = input('Ingrese la cantidad del nuevo producto: ')
    lista_producto = []
    lista_producto.extend((producto_nombre,producto_precio,producto_cantidad))
    linea = ','.join(lista_producto)
    return linea

def agregar_linea(linea_string):
    with open('productos.txt','a',encoding='utf-8') as archivo:
        archivo.write(linea_string)



# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

def cargar_productos_lista_dicc():
    lista = []
    try:
        with open('productos.txt','r',encoding='utf-8') as archivo:
            for linea in archivo:
                try:
                    datos = linea.strip().split(',')
                    nombre = datos[0]
                    precio = datos[1]
                    cantidad = datos[2]
                    dicc = {'nombre':nombre,'precio':precio,'cantidad':cantidad}
                    lista.append(dicc)
                except IndexError:
                    print('Se salteo una linea porque faltan datos!')
    except FileNotFoundError:
        print('El archivo no existe!')
    except PermissionError:
        print('No se tiene permisos para acceder al archivo!')
    return lista
productos = cargar_productos_lista_dicc()

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

def buscar_producto(lista):
    busqueda = input('Ingrese el nombre del producto que desea buscar: ')
    encontrado = False
    for i in range(len(lista)):
        if lista[i]['nombre'] == busqueda:
            encontrado = True
            print(f'Producto: {lista[i]['nombre']} | Precio: ${lista[i]['precio']} | Cantidad: {lista[i]['cantidad']}')
    if not encontrado:
        print('No se encontro el producto')

buscar_producto(productos)

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.
productos = [
    {"nombre": "Leche", "precio": 1.20, "cantidad": 30},
    {"nombre": "Pan de molde", "precio": 2.10, "cantidad": 15},
    {"nombre": "Café soluble", "precio": 4.50, "cantidad": 8},
    {"nombre": "Arroz 1kg", "precio": 1.80, "cantidad": 40}
]
def guardar_cambios(lista):
    with open('productos.txt','w',newline='',encoding='utf-8') as archivo:
        for dic in lista:
            lista_linea = []
            for v in dic.values():
                lista_linea.append(str(v))
            str_linea = ','.join(lista_linea)
            archivo.write(str_linea + '\n')
guardar_cambios(productos)
