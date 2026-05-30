funciones = [{'titulo':'Mortal Kombat','reservas':50,'lugares':50}]

def input_int(mensaje,mensaje_error):
    try:
        dato = int(input(mensaje))
        return dato
    except ValueError:
        print(mensaje_error)

def input_alpha_num(mensaje,mensaje_error):
    try:
        dato = input(mensaje).strip()
        if not dato.replace(' ','').isalnum():
            raise ValueError
        return dato.title()
    except ValueError:
        print(mensaje_error)

def mostrar_funciones(lista):
    if not lista:
        print('No hay funciones')
        return
    for funcion in lista:
        print(f'La función {funcion['titulo']} tiene {funcion['reservas']} reservas y los lugares totales son {funcion['lugares']}')

def buscar_pelicula(lista):
    if not lista:
        print('No hay funciones')
        return
    encontrado = False
    busqueda = input_alpha_num('Ingrese el titulo de la pelicula que desea buscar: ','Por favor ingrese un nombre correcto')
    while not busqueda:
        busqueda = input_alpha_num('Ingrese el titulo de la pelicula que desea buscar: ','Por favor ingrese un nombre correcto')
    for pelicula in lista:
        if pelicula['titulo'].startswith(busqueda):
            encontrado = True
            print(f'La pelicula {pelicula['titulo']} tiene {pelicula['reservas']} reservas y los lugares totales son {pelicula['lugares']}')
    if not encontrado:
        print('No se encontraron peliculas con ese nombre')

def agregar_funcion(lista):
    titulo = input_alpha_num('Ingrese el titulo de la pelicula que desea agregar: ','Por favor ingrese un nombre correcto')
    while not titulo:
        titulo = input_alpha_num('Ingrese el titulo de la pelicula que desea buscar: ','Por favor ingrese un nombre correcto')
    if not titulo in [f['titulo'].title() for f in lista]:
        cant_reservas = input_int('Ingrese la cantidad de reservas: ','Ingrese un numero correcto!')
        while not cant_reservas:
            cant_reservas = input_int('Ingrese la cantidad de reservas: ','Ingrese un numero correcto!')
        cant_lugares = input_int('Ingrese la cantidad total de lugares: ','Ingrese una cantidad correcta')
        while not cant_lugares:
            cant_lugares = input_int('Ingrese la cantidad de reservas: ','Ingrese un numero correcto!')
        nueva_funcion = {'titulo':titulo,'reservas':cant_reservas,'lugares':cant_lugares}
        lista.append(nueva_funcion)
        return lista
    print('La función ya existe!')
    return lista

def reservar_entrada(lista):
    if not lista:
        print('No hay funciones')
    encontrado = False
    titulo = input_alpha_num('Ingrese el titulo de la pelicula que desea agregar: ','Por favor ingrese un nombre correcto')
    while not titulo:
        titulo = input_alpha_num('Ingrese el titulo de la pelicula que desea buscar: ','Por favor ingrese un nombre correcto')
    for pelicula in lista:
        if titulo == pelicula['titulo']:
            encontrado = True
            if (pelicula['lugares'] - pelicula['reservas']) > 0:
                pelicula['reservas'] += 1
                print('Reserva realizada con exito')
                return lista
            else:
                print('Funcion llena!')
    if not encontrado:
        print('No se encontro la funcion')
    return lista


while True:
    print('''
1. Mostrar funciones
2. Buscar película
3. Agregar función
4. Reservar entrada
5. Cancelar reserva
6. Eliminar función
7. Reporte de ocupación
0. Salir
        ''')
    opcion = input_int('Ingrese una opcion: ','Ingrese un numero correcto')
    match opcion:
        case 1:
            mostrar_funciones(funciones)
        case 2:
            buscar_pelicula(funciones)
        case 3:
            funciones = agregar_funcion(funciones)
        case 4:
            funciones = reservar_entrada(funciones)
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 0:
            print('Saliendo del programa')
            break
        case _:
            print('Ingrese una opción correcta!')