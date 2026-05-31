

def input_int(mensaje):
    ''''En esta funcion valido que el dato ingresado sea un numero y lo castea a int'''
    while True:
        try:
            dato = int(input(mensaje))
            if dato < 0:
                raise ValueError
            return dato
        except ValueError:
            print('Error ingrese un numero correcto')

def input_str(mensaje):
    ''' En esta funcion valido que sea una cadena alfanumerica y no se agreguen caracteres especiales,
    ya que una herramienta podria tener un nombre que inlcuya un numero'''
    try:
        dato = input(mensaje).strip()
        if not dato.replace(' ','').isalnum():
            raise ValueError
        else:
            return dato.title()
    except ValueError:
        print('Ingrese un nombre correcto!')

def cargar_herramientas(inventario):
    '''Carga herramientas de forma inicial en caso de que no este inicializada la lista, de forma masiva'''
    try:
        if inventario:
            raise ValueError
        cantidad = input_int('Ingrese la cantidad de heramientas que desea cargar: ')
        for _ in range(cantidad):
            while True:
                herramienta = alta_producto(inventario)
                if herramienta != None:
                    inventario.append(herramienta)
                    break
    except ValueError:
        print('La lista ya ha sido inicializada, para cargar una nueva herramienta utilice la opcion 5 ')

def mostrar_inventario(inventario):
    '''Muestra todo el inventario herramienta por herramienta'''
    try:
        if not inventario:
            raise Exception
        for herramienta in inventario:
            print('-'*50)
            for k,v in herramienta.items():
                print(f'{k} : {v} Unidades')
            print('-'*50)
    except Exception:
        print('La lista de herramientas aun no esta inicializada')

def alta_producto(inventario):
    ''' Pide al usuario un nombre de herramienta y el stock y valida que no este en el inventario'''
    try:
        nombre = input_str('Ingrese el nombre de la herramienta a cargar: ')
        if nombre == None:
            raise TypeError
        if nombre.title() in [h['herramienta'].title() for h in inventario]:
            raise ValueError
        cantidad = input_int('Ingrese la cantidad de stock: ')
        print('Herramienta cargada con exito!')
        return {'herramienta':nombre,'cantidad':cantidad}
    except ValueError:
        print('La herramienta ya existe en el inventario')
    except TypeError:
        print('Error de tipo')

def consultar_stock(inventario):
    '''Consulta el stock de cierta herramienta en especifico'''
    try:
        if not inventario:
            raise Exception
        else:
            busqueda = input_str('Ingrese la herramienta que desea buscar: ')
            if busqueda == None:
                return
            encontrado = False
            for herramienta in inventario:
                if busqueda == herramienta['herramienta']:
                    encontrado = True
                    print('-'*50)
                    print(f'{herramienta['herramienta']} : {herramienta['cantidad']} unidades')
                    print('-'*50)
            if not encontrado:
                print('La herramienta no se encuentra en el catalogo!')
    except Exception:
        print('La lista aun no ha sido inicializada')

def reporte_agotados(inventario):
    '''Reporta solamente los agotados'''
    try:
        if not inventario:
            raise Exception
        agotado = False
        for herramienta in inventario:
            if herramienta['cantidad'] == 0:
                agotado = True
                print('-'*50)
                print(f'{herramienta['herramienta']} : {herramienta['cantidad']} unidades')
                print('-'*50)
        if not agotado:
            print('No hay productos agotados')
    except Exception:
        print('La lista aun no ha sido inicializada')

def actualizar_stock(inventario):
    '''Realiza la venta o ingreso de una herramienta'''
    try:
        if not inventario:
            raise Exception
        encontrado = False
        busqueda = input_str('Ingrese el nombre de la herramienta que desea actualizar: ')
        if busqueda == None:
            return
        for herramienta in inventario:
            if herramienta['herramienta'].title() == busqueda:
                encontrado = True
                print('''
                    1. Venta
                    2. Ingreso
                    ''')
                opcion = input_int('Ingrese una opcion: ')
                match opcion:
                    case 1:
                        cant = input_int('Ingrese la cantidad que desea vender: ')
                        if (herramienta['cantidad'] - cant) >= 0:
                            herramienta['cantidad'] -= cant
                            print('Venta realizada con exito!')
                        else:
                            print('No hay suficientes existencias')
                    case 2:
                        cant = input_int('Ingrese la cantidad que desea ingresar: ')
                        herramienta['cantidad'] += cant
                        print('Ingreso realizado con exito')
                    case _:
                        print('Opcion incorrecta')
        if not encontrado:
            print('No se encontro la herramienta')
    except Exception:
        print('La lista aun no ha sido inicializada')

# inventario = [{'herramienta':'Martillo','cantidad':0}]
inventario = []

while True:
    print('''
        1. Carga de Herramientas con Existencias Iniciales
        2. Visualización de Inventario
        3. Consulta de Stock
        4. Reporte de Agotados
        5. Alta de Nuevo Producto
        6. Actualización de Stock (Venta / Ingreso)
        7. Salir
        ''')
    
    opcion = input_int('Ingrese una opcion: ')
    match opcion:
        case 1:
            cargar_herramientas(inventario)
        case 2:
            mostrar_inventario(inventario)
        case 3:
            consultar_stock(inventario)
        case 4:
            reporte_agotados(inventario)
        case 5:
            try:
                nueva_herramienta = alta_producto(inventario)
                if nueva_herramienta:
                    inventario.append(nueva_herramienta)
                else:
                    raise ValueError
            except ValueError:
                print('No se agrego la herramienta')
        case 6:
            actualizar_stock(inventario)
        case 7:
            print('Saliendo del programa!')
            break
        case _:
            print('Ingrese una opcion correcta!')