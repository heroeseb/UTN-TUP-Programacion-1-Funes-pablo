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
def crear_linea():
    producto_nombre = input('Ingrese el nombre del nuevo producto: ')
    producto_precio = input('Ingrese el precio del nuevo producto: ')
    producto_cantidad = input('Ingrese la cantidad del nuevo producto: ')
    
    lista_producto = [producto_nombre, producto_precio, producto_cantidad]
    # Agregamos el salto de línea al final para mantener el archivo ordenado
    linea = ','.join(lista_producto) + '\n'
    return linea

def agregar_linea(linea_string):
    with open('productos.txt', 'a', encoding='utf-8') as archivo:
        archivo.write(linea_string)


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
                    nombre = datos[0]
                    # Convertimos a float e int para que la lista tenga los tipos correctos
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
    busqueda = input('Ingrese el nombre del producto que desea buscar: ')
    encontrado = False
    
    # Una forma más directa en Python de recorrer la lista sin usar range(len())
    for producto in lista:
        if producto['nombre'].lower() == busqueda.lower(): # .lower() evita problemas con mayúsculas
            encontrado = True
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            break # Si lo encuentra, detenemos el ciclo
            
    if not encontrado:
        print('No se encontró el producto')


# =====================================================================
# 6. Guardar los productos actualizados
# =====================================================================
def guardar_cambios(lista):
    with open('productos.txt', 'w', newline='', encoding='utf-8') as archivo:
        for dic in lista:
            lista_linea = []
            for v in dic.values():
                lista_linea.append(str(v))
            str_linea = ','.join(lista_linea)
            archivo.write(str_linea + '\n')


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
    # Para probar la consigna 6, modificamos un dato en memoria antes de guardar
    if productos:
        print("Modificando la cantidad del primer producto en la lista para verificar el guardado...")
        productos[0]['cantidad'] += 10 
        
    guardar_cambios(productos)
    print("Archivo 'productos.txt' actualizado correctamente con los datos de la lista.")