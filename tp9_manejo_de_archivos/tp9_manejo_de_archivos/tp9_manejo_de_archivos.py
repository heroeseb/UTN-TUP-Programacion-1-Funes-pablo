from fcs_manejor_de_archivos import *

# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
p1 = "Lapicera,120.5,30\n"
p2 = "Cuaderno,450.0,15\n"
p3 = "Goma,80.25,50\n"
try:
    with open('productos.txt','w',encoding='utf-8') as archivo:
        archivo.write(p1)
        archivo.write(p2)
        archivo.write(p3)
except TypeError:
    print('Solo se puede ingresar datos del tipo String!')
'''
.write() solo puede recibir string de otra forma tira un error de tipo
'''
# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30
with open('productos.txt','r',encoding='utf-8') as archivo:
    for linea in archivo:
        datos = linea.strip().split(',')
        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        print(f'Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}')
# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.
producto = input('Ingrese un nuvo producto(nombre,precio,cantidad) separado por comas: ')
with open('productos.txt','a',encoding='utf-8') as archivo:
    archivo.write(producto + "\n")


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.
# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.
# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.
# Consejo final:
# Antes de empezar, analizá cada problema y pensá cómo dividirlo en partes:
# ● Leer archivo
# ● Procesar datos
# ● Mostrar o actualizar información
# ● Guardar los cambios
# Al terminar, probá tu programa varias veces:
# ● ¿Se puede agregar más de un producto?
# ● ¿Se guarda todo correctamente?
# ● ¿Se muestra bien el resultado?