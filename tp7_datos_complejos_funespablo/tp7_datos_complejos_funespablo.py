# Ejercicio 1
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

# Ejercicio 2
print('Ejercicio 2')

precios_frutas['Banana']  = 1330
precios_frutas['Manzana']  = 1700
precios_frutas['Melón']  = 2800

print('Diccionario con precios de Banana, Manzana y Melón actualizados:')
mostrar_elementos(precios_frutas)
print('-'*50)

# Ejercicio 3
print('Ejercicio 3')

def print_valores_lista(lista):
    print(*lista,sep=' , ')

lista_values_precio_frutas = list(precios_frutas.keys())
print('Lista de frutas: ')
print_valores_lista(lista_values_precio_frutas)
print('-'*50)

# Ejercicio 4
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
        1. Almacenar número telefónico
        2. Consultar número telefónico
        3. Salir
        ''')
    opcion = input_int('Elige una opción: ','Ingrese un número correcto!')
    
    match opcion:
        case '1':
            for _ in range(cantidad_repeticiones):
                nombre = input_string('Ingrese el nombre del contacto: ','Ingrese un nombre correcto')
                numero = input_int('Ingrese el número de teléfono: ','Ingrese un número correcto!')
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
                print('Aún no tienes ningún contacto agendado')

        case '3':
            print('Saliendo del programa')
            break

        case _:
            print('Ingrese una opción correcta!')

# Ejercicio 5
print('-'*50)
print('Ejercicio 5')

frase = input_string('Dime una frase: ','Solo se permiten letras!')
lista_frase = frase.lower().split()
set_frase = set(lista_frase)
dict_frase = {}

print('Las palabras únicas son: ')
for palabra in set_frase:
    if palabra != '':
        print(palabra,end=' ')
print()

for palabra in lista_frase:
    if palabra in dict_frase:
        dict_frase[palabra] += 1
    else:
        dict_frase[palabra] = 1

print('La cantidad de veces que aparece cada palabra es: ')
mostrar_elementos(dict_frase)

# Ejercicio 6
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
                    nota = input_entero_convert(f'Ingresa la nota {j+1}: ','Ingresa solo números!')
                    if nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print('El número debe ser menor o igual a 10')
            dict_alumnos[nombre_alumno] = tuple(notas)
            break
        else:
            print('El nombre ya está en la lista!')
        
print('Los promedios de los alumnos son: ')
for k,v in dict_alumnos.items():
    print(f'- {k} : {sum(v)/len(v):.2f}')

# Ejercicio 7
print('-'*50)
print('Ejercicio 7')

print('Lista de asistencia original: ')
asistencias = [
    "Ana", "Luis", "Marta", "Ana", "Carlos",
    "Luis", "Ana", "Marta", "Pedro", "Luis",
    "Sofía", "Carlos", "Ana", "Pedro", "Sofía",
    "Marta", "Luis", "Ana"
]

print(*asistencias,sep=' , ')

set_asistencia = set(asistencias)

print('Empleados que asistieron al menos una vez: ')
print(*set_asistencia,sep=' , ')

for empleado in set_asistencia:
    print(f'Empleado {empleado} asistió: {asistencias.count(empleado)} veces')

# Ejercicio 8
print('-'*50)
print('Ejercicio 8')

productos_stock_diccionario = {}

while True:
    print('''
        Menú:
        1. Consultar el stock de un producto
        2. Agregar unidades al stock
        3. Agregar nuevo producto
        4. Salir
        ''')
    opcion = input_int('Ingresa una opción: ','Ingresa solo números!')
    
    match opcion:
        case '1':
            if productos_stock_diccionario:
                producto = input_string('Ingresa el nombre del producto: ','Ingresa un nombre correcto!')
                if producto in productos_stock_diccionario:
                    print(f'El stock del producto {producto} es {productos_stock_diccionario[producto]}')
                else:
                    print('El producto no está en stock')
            else:
                print('Aún no se ha inicializado el diccionario!')

        case '2':
            if productos_stock_diccionario:
                producto = input_string('Ingresa el nombre del producto: ','Ingresa un nombre correcto!')
                if producto in productos_stock_diccionario:
                    cantidad = input_entero_convert(f'Ingrese la cantidad de stock del producto {producto}: ','Ingrese un número correcto')
                    productos_stock_diccionario[producto] = cantidad
                    print('Stock agregado correctamente!')
                else:
                    print('El producto no está en stock')
            else:
                print('Aún no se ha inicializado el diccionario!')

        case '3':
            producto = input_string('Ingresa el nombre del producto que deseas agregar: ','Ingresa un nombre correcto!')
            if not producto in productos_stock_diccionario:
                cantidad = input_entero_convert(f'Ingrese la cantidad de stock del producto a ingresar: ','Ingrese un número correcto')
                productos_stock_diccionario[producto] = cantidad
                print('Producto agregado correctamente!')
            else:
                print('El producto ya está en inventario, si quieres agregar stock usa opción 2!')

        case '4':
            print('Saliendo del programa')
            break

        case _:
            print('Ingresa una opción correcta!')

# Ejercicio 9
print('-'*50)
print('Ejercicio 9')

def esta_en_agenda(agenda_param,consultadia,consultahora):
    for (dia, hora), evento in agenda_param.items():
        if dia == consultadia and hora == consultahora:
            return evento
    return None

def es_digito(dato):
    if dato.replace(':','',1).isdigit():
        return True
    else:
        return False

agenda = {
    ("lunes", "09:00"): "Clase de matemáticas",
    ("lunes", "11:00"): "Reunión con equipo",
    ("martes", "10:00"): "Estudiar programación",
    ("miércoles", "15:00"): "Gimnasio",
    ("jueves", "08:30"): "Consulta médica",
    ("viernes", "20:00"): "Salida con amigos"
}

consulta_dia = input_string('¿Qué día deseas consultar en la agenda?: ','Ingresa solo letras!').lower()
consulta_hora = input('Ingresa la hora que deseas consultar: ').strip()

while not (len(consulta_hora[:2]) == 2 and len(consulta_hora[3:]) == 2 and consulta_hora.count(':') == 1 and es_digito(consulta_hora)):
    print('Ingrese una hora correcta!')
    consulta_hora = input('Ingresa la hora que deseas consultar: ')

evento_agenda = esta_en_agenda(agenda,consulta_dia,consulta_hora)

if evento_agenda:
    print(f'El día {consulta_dia} a las {consulta_hora} tiene la actividad: {evento_agenda}')
else:
    print('Agenda vacía en ese día y horario!')

# Ejercicio 10
print('-'*50)
print('Ejercicio 10')

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia",
    "Paraguay": "Asunción",
    "Perú": "Lima",
    "Bolivia": "Sucre",
    "Colombia": "Bogotá",
    "Ecuador": "Quito",
    "Venezuela": "Caracas"
}

print('Diccionario original: ')
mostrar_elementos(paises_capitales)

def diccionario_invertido(diccionario):
    dic_retorno = {}
    for k,v in diccionario.items():
        dic_retorno[v] = k
    return dic_retorno

nuevo_capitales_paises = diccionario_invertido(paises_capitales)

print('Diccionario con valores invertidos: ')
mostrar_elementos(nuevo_capitales_paises)