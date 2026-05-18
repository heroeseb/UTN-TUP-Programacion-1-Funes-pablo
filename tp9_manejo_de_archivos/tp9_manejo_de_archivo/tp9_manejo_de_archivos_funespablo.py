# =====================================================================
# 1. Crear archivo inicial con productos
# =====================================================================
p1 = "Lapicera,120.5,30\n"
p2 = "Cuaderno,450.0,15\n"
p3 = "Goma,80.25,50\n"

def crear_archivo_txt(l1, l2, l3):
    '''
    .write() solo puede recibir string de otra forma tira un error de tipo
    '''
    try:
        with open('productos.txt', 'w', encoding='utf-8') as archivo:
            archivo.write(l1)
            archivo.write(l2)
            archivo.write(l3)
    except TypeError:
        print('Solo se puede ingresar datos del tipo String!')


# =====================================================================
# 2. Leer y mostrar productos
# =====================================================================
def leer_mostrar_productos():
    try:
        with open('productos.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                try:
                    datos = linea.strip().split(',')
                    if len(datos) != 3:
                        print(f'Línea omitida por formato incorrecto (deben ser 3 columnas): {linea.strip()}')
                        continue
                    nombre = datos[0]
                    precio = float(datos[1])
                    cantidad = int(datos[2])
                    print(f'Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}')
                except IndexError:
                    print('Se salteó una línea porque faltan datos!')
    except FileNotFoundError:
        print('El archivo no existe!')
    except PermissionError:
        print('No se tiene permisos para acceder al archivo!')


# =====================================================================
# 3. Agregar productos desde teclado
# =====================================================================
def input_str(mensaje,mensaje_2=None):
    while True:
        try:
            input_salid = input(mensaje).strip()
            if not input_salid.replace(' ','').isalnum():
                raise TypeError
            return input_salid
        except TypeError:
            print(mensaje_2 if mensaje_2 else 'Error de tipo')

def input_int_or_float(tipo,mensaje,mensaje_2=None):
    while True:
        try:
            match tipo:
                case 'int':
                    input_salid = input(mensaje).strip()
                    if not (input_salid.isdigit() and int(input_salid) >= 0):
                        raise ValueError
                    return input_salid
                case 'float':
                    input_salid = input(mensaje).strip()
                    if not (input_salid.replace('.','',1).isdigit() and float(input_salid) > 0):
                        raise ValueError
                    return input_salid
        except ValueError:
            print(mensaje_2 if mensaje_2 else 'Error de valor')

def crear_linea():
    producto_nombre = input_str('Ingrese el nombre del nuevo producto: ','Ingrese un nombre correcto!')
    producto_precio = input_int_or_float('float','Ingrese el precio del nuevo producto: ','Ingrese un precio correcto')
    producto_cantidad = input_int_or_float('int','Ingrese la cantidad del nuevo producto: ','Ingrese una cantidad correcta')
    lista_producto = [producto_nombre.capitalize(), producto_precio, producto_cantidad]
    linea = ','.join(lista_producto) + '\n'
    return linea

def agregar_linea(linea_string):
    try:
        with open('productos.txt', 'a', encoding='utf-8') as archivo:
            archivo.write(linea_string)
    except PermissionError:
        print('No se tiene permisos para acceder al archivo!')


# =====================================================================
# 4. Cargar productos en una lista de diccionarios
# =====================================================================
def cargar_productos_lista_dicc():
    lista = []
    try:
        with open('productos.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                if not linea.strip():
                    continue
                try:
                    datos = linea.strip().split(',')
                    if len(datos) != 3:
                        print(f'Línea omitida por formato incorrecto (deben ser 3 columnas): {linea.strip()}')
                        continue
                    nombre = datos[0]
                    precio = float(datos[1])
                    cantidad = int(datos[2])
                    
                    dicc = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
                    lista.append(dicc)
                except IndexError:
                    print('Se salteó una línea porque faltan datos!')
                except ValueError:
                    print('Error de formato en números al cargar una línea.')
    except FileNotFoundError:
        print('El archivo no existe!')
    except PermissionError:
        print('No se tiene permisos para acceder al archivo!')
    return lista


# =====================================================================
# 5. Buscar producto por nombre
# =====================================================================
def buscar_producto(lista):
    if not lista:
        print("La lista de productos está vacía. No hay nada que buscar.")
        return
    busqueda = input('Ingrese el nombre del producto que desea buscar: ').strip()
    encontrado = False
    for producto in lista:
        if producto['nombre'].capitalize() == busqueda.capitalize(): 
            encontrado = True
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            break 
    if not encontrado:
        print('No se encontró el producto')


# =====================================================================
# 6. Guardar los productos actualizados
# =====================================================================

def guardar_cambios(lista):
    try:
        with open('productos.txt', 'w', newline='', encoding='utf-8') as archivo:
            for dic in lista:
                lista_linea = [str(v) for v in dic.values()]
                str_linea = ','.join(lista_linea)
                archivo.write(str_linea + '\n')
    except PermissionError:
        print('¡Error! No se pudo guardar. El archivo está abierto por otro programa o no hay permisos.')


# =====================================================================
# FLUJO PRINCIPAL DE EJECUCIÓN (Ejecuta cada consigna en orden)
# =====================================================================
if __name__ == "__main__":
    print("--- 1. Creando archivo inicial ---")
    crear_archivo_txt(p1, p2, p3)
    print("Archivo creado con éxito.\n")

    print("--- 2. Leyendo y mostrando productos iniciales ---")
    leer_mostrar_productos()
    print()

    print("--- 3. Agregando producto desde teclado al archivo ---")
    nueva_linea = crear_linea()
    agregar_linea(nueva_linea)
    print("Producto agregado al archivo.\n")

    print("--- 4. Cargando todos los productos del archivo a la lista ---")
    productos = cargar_productos_lista_dicc()
    print(f"Lista cargada en memoria. Total productos: {len(productos)}\n")

    print("--- 5. Buscando un producto en la lista ---")
    buscar_producto(productos)
    print()

    print("--- 6. Guardando cambios/sobrescribiendo archivo desde la lista ---")
    # Para probar modificamos un dato en memoria antes de guardar
    if productos:
        print("Modificando la cantidad del primer producto en la lista para verificar el guardado...")
        productos[0]['cantidad'] += 10 
        
    guardar_cambios(productos)
    print("Archivo 'productos.txt' actualizado correctamente con los datos de la lista.")
