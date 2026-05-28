
biblioteca = []
biblioteca = [{'titulo':'Romper el circulo','copias':1}]

def es_entero(mensaje,mensaje_error):
    while True:
        try:
            dato = int(input(mensaje))
            return dato
        except ValueError:
            print(mensaje_error)

def input_alpha_num(mensaje,mensaje_error):
    while True:
        try:
            dato = input(mensaje).strip()
            if not dato.replace(' ','').isalnum():
                raise ValueError
            else:
                return dato
        except ValueError:
            print(mensaje_error)

def buscar_en_dicc(dato,lista,key):
    if dato.capitalize() in [e[key].capitalize() for e in lista]:
        return True
    return False

def cargar_libro(lista_biblioteca):
    libro = input_alpha_num('Ingrese el nombre del titulo: ','Ingrese un nombre correcto')
    libro_no_esta = False
    if not( buscar_en_dicc(libro,lista_biblioteca,'titulo')):
        libro_no_esta = True
        cant_copias = es_entero('Ingrese la cantidad de copias del titulo: ','Ingrese un numero correcto')
        nuevo_libro = {'titulo': libro.capitalize(), 'copias': cant_copias}
        print('libro cargado correctamente')
        return nuevo_libro
    if not libro_no_esta:
        print('El libro ya esta cargado en la lista')

def carga_varios_libros(lista_biblioteca):
    cant_carga = es_entero('Ingrese la cantidad de libros que desea cargar: ','Ingrese un numero correcto')
    for _ in range (cant_carga):
        nuevo_libro = cargar_libro(lista_biblioteca)
        if nuevo_libro :
            lista_biblioteca.append(nuevo_libro)
    return lista_biblioteca

def mostrar_catalogo(lista_biblioteca):
    if not lista_biblioteca:
        print('No esta iniciada la lista de titulos...')
        return
    print('Lista completa de titulos')
    for libro in lista_biblioteca:
        print('-'*50)
        for k,v in libro.items():
            print(f'{k} : {v}')
        print('-'*50)

def buscar_libro(lista_biblioteca):
    if not lista_biblioteca:
        print('No esta iniciada la lista de titulos...')
        return
    busqueda = input_alpha_num('Ingrese el nombre del titulo que desea buscar: ','Ingrese un nombre correcto!')
    if buscar_en_dicc(busqueda,lista_biblioteca,'titulo'):
        for libro in biblioteca:
            if busqueda.capitalize() == libro['titulo']:
                print(f'El libro {busqueda.capitalize()} se encuentra con un stock de {libro['copias']} copias')
                return
    print('No se encontro el libro!')

def agotado(lista_biblioteca):
    if not lista_biblioteca:
        print('La lista aun no ha sido inicilaizada')
        return
    hay_agotados = False
    for libro in lista_biblioteca:
        if libro['copias'] <= 0:
            if not hay_agotados:
                print('La lista de agotados es: ')
            print('-'*50)
            hay_agotados = True
            print(f'{libro['titulo']} agotado')
            print('-'*50)
    if not hay_agotados:
        print('No hay titulos agotados')

def prestar_devolver(lista_biblioteca):
    if not lista_biblioteca:
        print('No esta iniciada la lista de titulos...')
        return
    while True:
        print('1. Prestar')
        print('2. Devolver')
        print('3. Salir')
        opcion = es_entero('Ingrese una opcion: ','Ingrese una opcion correcta')
        match opcion:
            case 1:
                titulo = input_alpha_num('Ingrese el nombre del titulo a Prestar: ','Ingrese un nombre correcto')
                for libro in lista_biblioteca:
                    if titulo.capitalize() == libro['titulo'].capitalize():
                        if libro['copias'] > 0:
                            libro['copias'] -= 1
                            print(f'Libro {libro['titulo']} prestado con exito, el stock actual es {libro['copias']}')
                            return lista_biblioteca
                        else:
                            print('No hay suficientes copias en stock para prestar')
                            return lista_biblioteca
                print('No se encontro el titulo')
            case 2:
                titulo = input_alpha_num('Ingrese el nombre del titulo a Devolver: ','Ingrese un nombre correcto')
                for libro in lista_biblioteca:
                    if titulo.capitalize() == libro['titulo'].capitalize():
                        libro['copias'] += 1
                        print(f'Libro {libro['titulo']} devuelto con exito, el stock actual es {libro['copias']}')
                        return lista_biblioteca
                print('No se encontro el titulo')
            case 3:
                print('Volviendo al menu principal')
                return lista_biblioteca
            case _:
                print('Opcion ingresada incorrecta')

while True:
    print('''
    1. Carga inicial: Preguntar cuántos libros se van a registrar por primera vez. Por cada uno, pedir el título y la 
    cantidad de copias.
    2. Ver catálogo: Recorrer nuestra lista y mostrar todos los libros con su cantidad de copias actuales.
    3. Buscar libro: El usuario escribe un título y le decimos si lo tenemos y cuántas copias quedan. ¡Avisar 
    amablemente si no lo tenemos!
    4. Alerta de agotados: Mostrar solo aquellos libros que tienen 0 copias para saber cuáles hay que reponer.
    5. Sumar un título nuevo: Agregar un nuevo diccionario a la lista con su título y cantidad de copias.
    6. Prestar o Devolver (Actualizar): Modificar las copias de un libro que ya existe. Si lo prestamos, restamos uno; 
    si lo devuelven, sumamos uno.
    7. Salir de la biblioteca.
        ''')
    opcion = es_entero('Ingrese una opción: ','Ingrese un numero correcto')
    match opcion:
        case 1:
            biblioteca = carga_varios_libros(biblioteca)
        case 2:
            mostrar_catalogo(biblioteca)
        case 3:
            buscar_libro(biblioteca)
        case 4:
            agotado(biblioteca)
        case 5:
            nuevo_libro = cargar_libro(biblioteca)
            if not (nuevo_libro == None):
                biblioteca.append(nuevo_libro)
        case 6:
            biblioteca = prestar_devolver(biblioteca)
        case 7:
            print('saliendo del programa!')
            break
        case _:
            print('Ingrese una opcion correcta!')
