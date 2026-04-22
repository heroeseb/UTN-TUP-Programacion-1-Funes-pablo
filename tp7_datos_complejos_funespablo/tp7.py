# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450}
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300

print('-'*50)
print('Ejercicio 1')

def mostrar_elementos(iterable):
    for k,v in iterable.items():
        print(f'{k} : {v}')

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

mostrar_elementos(precios_frutas)

precios_frutas['Naranja']  = 1200
precios_frutas['Manzana']  = 1500
precios_frutas['Pera']  = 2300

print()
print('Diccionario con nuevos valores: ')
mostrar_elementos(precios_frutas)
print('-'*50)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800

print('Ejercicio 2')

precios_frutas['Banana']  = 1330
precios_frutas['Manzana']  = 1700
precios_frutas['Melón']  = 2800

print('Diccionario con precios de Banana,Manzana y Melón actualizados:')
mostrar_elementos(precios_frutas)
print('-'*50)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios.

print('Ejercicio 3')
def print_valores_lista(lista):
    print(*lista,sep=' , ')
lista_values_precio_frutas = list(precios_frutas.keys())
print('Lista de frutas: ')
print_valores_lista(lista_values_precio_frutas)
print('-'*50)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

print('Ejercicio 4')
def input_int(mensaje,mensaje2):
    while True:
        opcion = input(mensaje).strip()
        if opcion.replace('.','',1).isdigit() and float(opcion) > 0:
            return opcion
        else:
            print(mensaje2)
def input_string(mensaje,mensaje2):
    while True:
        opcion = input(mensaje).strip()
        if opcion.replace(" ","").isalpha():
            return opcion.capitalize()
        else:
            print(mensaje2)

dic_numeros_tel = {}
while True:
    cantidad_repeticiones = 5
    print('''
        1. Almacenar Número telefónico
        2. Consultar Número telefónico
        3. Salir
        ''')
    opcion = input_int('Elige una opcion: ','Ingrese un número correcto!')
    match opcion:
        case '1':
            for _ in range(cantidad_repeticiones):
                nombre = input_string('Ingrese el nombre del contacto: ','Ingrese un nombre correcto')
                numero = input_int('Ingrese el número de telefono: ','Ingrese un número correcto!')
                dic_numeros_tel[nombre] = numero
                print(f'Contacto {nombre} ingresado correctamente')
        case '2':
            if dic_numeros_tel:
                nombre = input_string('Ingrese el nombre del contacto a buscar: ','Ingrese un nombre correcto')
                if nombre in dic_numeros_tel:
                    print('Contacto: ')
                    print(f"{nombre} : número {dic_numeros_tel[nombre]}")
                else:
                    print('No tienes agendado a nadie con ese nombre!')
            else:
                print('Aun no tienes ningun contacto agendado')
        case '3':
            print('Saliendo del programa')
            break
        case _:
            print('Ingrese una opción correcta!')

# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra
print('-'*50)
print('Ejercicio 5')
frase = input_string('Dime un frase: ','Solo se permiten letras!')
lista_frase = frase.lower().split()
set_frase = set(lista_frase)
dict_frase = {}
print('Las palabras unicas son: ')
for palabra in set_frase:
    if not palabra == '':
        print(palabra,end=' ')
print()
for palabra in lista_frase:
    if palabra in dict_frase:
        dict_frase[palabra] += 1
    else:
        dict_frase[palabra] = 1
print('La cantidad de veces que aparece cada palabra es: ')
mostrar_elementos(dict_frase)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, 
# mostrá el promedio de cada alumno.
print('-'*50)
print('Ejercicio 6')
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

dict_alumnos = {}

for i in range(3):
    notas = []
    while True:
        nombre_alumno = input_string(f'Ingresa el nombre del estudiante {i+1}: ','Ingresa solo letras para el nombre!')
        if not nombre_alumno in dict_alumnos:
            for j in range(3):
                while True:
                    nota = input_entero_convert(f'Ingresa la nota {j+1}: ','Ingresa solo numeros!')
                    if nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print('El numero debe ser menor de 10')
            dict_alumnos[nombre_alumno] = tuple(notas)
            break
        else:
            print('El nombre ya esta en la lista!')
        
print('Los promedios de los alumnos son: ')
for k,v in dict_alumnos.items():
    print(f'- {k} : {sum(v)/len(v):.2f}')

# 7) Se recibe el registro diario de asistencia a una capacitación en forma de lista.
# En dicha lista pueden aparecer nombres repetidos, ya que una misma persona pudo haber 
# asistido en más de una jornada.
# • Mostrá la lista original de asistencias.
# • Generá un conjunto (set) a partir de la lista y mostrar los empleados que asistieron al 
# menos una vez (sin repetir nombres).
# • Indicá cuántas veces asistió cada empleado a la capacitación.

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


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario:
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe.

productos_stock_diccionario = {}
while True:
    print('''
        Menu:
        1. Consultar el stock de un producto
        2. Agregar unidades al stock
        3. Agregar nuevo producto
        4. Salir
        ''')
    opcion = input_int('Ingresa una opción: ','Ingresa solo letras!')
    match opcion:
        case '1':
            if productos_stock_diccionario:
                producto = input_string('Ingresa el nombre del producto: ','Ingresa un nombre correcto!')
                if producto in productos_stock_diccionario:
                    print(f'El stock del producto {producto} es {productos_stock_diccionario[producto]}')
                else:
                    print('El producto no esta en stock')
            else:
                print('Aun no se ha inicializado el diccionario!')
        case '2':
            
        case '3':
            pass
        case '4':
            pass
        case _:
            pass