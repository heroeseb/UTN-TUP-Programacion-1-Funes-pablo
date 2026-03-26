# ALUMNO: Funes Pablo Sebastian

titulos = [] # Uso la variable sin tilde para así no equivocarme al llamarla
ejemplares = []
#titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
#ejemplares = [4, 10, 1]
while True:
    print('''
        -----------------------------------------------------------
        |                  MENÚ DE BIBLIOTECA                     |
        -----------------------------------------------------------
        ¬ 1 -> Ingresar títulos (carga inicial, pueden ser varios)
        ¬ 2 -> Mostrar catálogo
        ¬ 3 -> Consultar disponibilidad
        ¬ 4 -> Listar agotados
        ¬ 5 -> Agregar título (uno solo)
        ¬ 6 -> Actualizar ejemplares (préstamo/devolución)
        ¬ 7 -> Salir. 
        ''')
    opcion = input('Seleccioná una opción ( 1 - 7 ):  ')
    match opcion:
        case '1':
            cantidad_titulos = input("Dime la cantidad de títulos que ingresará: ").strip()
            if cantidad_titulos.isdigit():
                int_cantidad_titulos = int(cantidad_titulos)
                if int_cantidad_titulos > 0:
                    for i in range (int_cantidad_titulos):
                        while True:# Utilizo un while para que, en caso de ingresar un dato incorrecto o un título ya presente en la lista, me vuelvan a aparecer los input, dándome la oportunidad de volver a ingresar un dato correcto.
                            titulo_ingresado = input('Ingresa el nombre del título: ').strip()
                            no_esta_titulo = True
                            if titulos:# Valido que la lista no esté vacía
                                for titulo in titulos:# Lo hice con un bucle porque me había olvidado del uso de la palabra reservada "in"
                                    if titulo.lower() == titulo_ingresado.lower():
                                        no_esta_titulo = False
                                        break
                            if no_esta_titulo:
                                cant_ejemplar = input('Ingresa la cantidad de ejemplares: ')
                                if cant_ejemplar.isdigit():
                                    int_cantidad_ejemplar = int(cant_ejemplar)
                                    if int_cantidad_ejemplar > 0:
                                        titulos.append(titulo_ingresado.title())
                                        ejemplares.append(int_cantidad_ejemplar)
                                        print('El título y cantidad de ejemplares agregados con éxito...')
                                        break
                                    else:
                                        print('Ingrese una cantidad de ejemplares mayor a 0 ...')
                                else:
                                    print('Ingrese un número válido...')
                            else:
                                print('El título ya está en la biblioteca, por favor ingrese otro...')
                else:
                    print('El número debe ser mayor a cero...')
            else:
                print('Ingrese un número correcto...')
        case '2':
            if titulos:
                print('Catálogo completo: ')
                for i in range(len(titulos)):
                    print(f'{i+1} - {titulos[i]} : {ejemplares[i]} ejemplares.')
            else:
                print('No hay títulos / aún no se ingresan títulos...')
        case '3':
            if titulos:
                print('''Consultar disponibilidad por:
                    1. Nombre del título
                    2. Mostrar el catálogo completo y seleccionar número de título''')
                opcion_metodo = input('Seleccionar opción (1 o 2): ').strip()
                match opcion_metodo:
                    case '1':
                        no_esta = True
                        titulo_consulta = input('Ingresa el nombre del título que quieres consultar disponibilidad: ').strip()
                        for i in range(len(titulos)):
                            if titulo_consulta.lower() == titulos[i].lower():
                                if ejemplares[i] > 0:
                                    print(f'El título "{titulos[i]}" tiene: {ejemplares[i]} ejemplares disponibles.')
                                    no_esta = False
                                    break
                                else:
                                    print(f'No hay ejemplares disponibles del título: "{titulos[i]}"')
                                    no_esta = False
                                    break
                        if no_esta:
                            print(f'El título "{titulo_consulta}" no está en el catálogo, o no está con ese nombre...')
                    case '2':
                        print('Catálogo completo: ')
                        for i in range(len(titulos)):
                            print(f'{i+1} - {titulos[i]}.')
                        opcion_numero_catalogo = input('Seleccione el número de título que desea consultar disponibilidad: ').strip()
                        if opcion_numero_catalogo.isdigit():
                            int_opcion_numero_catalogo = int(opcion_numero_catalogo)
                            if int_opcion_numero_catalogo >= 1 and len(titulos) >= int_opcion_numero_catalogo:
                                if ejemplares[int_opcion_numero_catalogo - 1] > 0 :
                                    print(f'El título "{titulos[int_opcion_numero_catalogo - 1]}" tiene: {ejemplares[int_opcion_numero_catalogo - 1]} ejemplares disponibles ')
                                else:
                                    print(f'No hay disponibilidad del título "{titulos[int_opcion_numero_catalogo - 1]}"')
                            else:
                                print('Número fuera del catálogo...')
                        else:
                            print('Debe ingresar un número válido...')
                    case _:
                        print('Ingrese una opción correcta...')
            else:
                print('No hay títulos / aún no se ingresan títulos...')
        case '4':
            if titulos:
                print('Lista de títulos agotados:')
                no_agotados = True
                for i in range(len(ejemplares)):
                    if ejemplares[i] == 0:
                        no_agotados = False
                        print(f'- "{titulos[i]}"')
                if no_agotados:
                    print('No hay títulos agotados...')
            else:
                print('No hay títulos / aún no se ingresan títulos...')
        case '5':
            titulo_individual_agregar = input('Ingresa el nombre del título a agregar: ').strip()
            no_esta = True
            if titulos:
                for titulo in titulos:
                    if titulo.lower() == titulo_individual_agregar.lower():
                        no_esta = False
                        break
            if no_esta:
                cantidad_ejemplar_individual = input('Ingrese la cantidad de ejemplares: ').strip()
                if cantidad_ejemplar_individual.isdigit():
                    int_cantidad_ejemplar_individual = int(cantidad_ejemplar_individual)
                    if int_cantidad_ejemplar_individual > 0:
                        titulos.append(titulo_individual_agregar.title())
                        ejemplares.append(int_cantidad_ejemplar_individual)
                        print('Título y cantidad de ejemplares agregados con éxito...')
                    else:
                        print('La cantidad de ejemplares debe ser mayor a 0...')
                else:
                    print('Ingrese un número válido...')
            else:
                print(f'El título: "{titulo_individual_agregar.title()}" ya está en la lista...')
        case '6':
            if titulos:
                print('''
                    1. Préstamo
                    2. Devolución
                    ''')
                opcion_prestamo_devolucion = input('Ingrese una opción (1 o 2): ').strip()
                match opcion_prestamo_devolucion:
                    case '1':
                        titulo_prestamo = input('Ingresa el título que quieres tomar prestado: ').strip()
                        no_esta = True
                        for i in range(len(titulos)):
                            if titulo_prestamo.lower() == titulos[i].lower():
                                no_esta = False
                                if ejemplares[i] > 0:
                                    cantidad_prestamo = input('Ingresa la cantidad de ejemplares que tomarás prestado: ').strip()
                                    if cantidad_prestamo.isdigit():
                                        int_cantidad_prestamo = int(cantidad_prestamo)
                                        if int_cantidad_prestamo > 0 :
                                            if ejemplares[i] >= int_cantidad_prestamo:
                                                ejemplares[i] = ejemplares[i] - int_cantidad_prestamo
                                                print(f'Se prestó {int_cantidad_prestamo} ejemplar/es del título "{titulos[i]}" con éxito.')
                                                print(f'Quedan {ejemplares[i]} ejemplar/es en biblioteca...')
                                            else:
                                                print('No hay suficientes ejemplares...')
                                        else:
                                            print('Ingrese un número mayor a 0...')
                                    else:
                                        print('Ingrese un número válido...')
                                else:
                                    print(f'El título "{titulos[i]}" está agotado...')
                                break
                        if no_esta:
                            print('El título no está en el catálogo... ingrese un título válido...')
                    case '2':
                        titulo_devolucion = input('Ingresa el título que quieres devolver: ').strip()
                        no_esta = True
                        for i in range(len(titulos)):
                            if titulo_devolucion.lower() == titulos[i].lower():
                                no_esta = False
                                cantidad_devolucion = input('Ingresa la cantidad de ejemplares que desea devolver: ').strip()
                                if cantidad_devolucion.isdigit():
                                    int_cantidad_devolucion = int(cantidad_devolucion)
                                    if int_cantidad_devolucion > 0 :
                                        ejemplares[i] = ejemplares[i] + int_cantidad_devolucion
                                        print(f'Devolvió {int_cantidad_devolucion} ejemplar/es del título "{titulos[i]}" con éxito.')
                                        print(f'Hay un total de {ejemplares[i]} ejemplar/es en biblioteca...')
                                    else:
                                        print('Ingrese un número mayor a 0...')
                                else:
                                        print('Ingrese un número válido...')
                                break
                        if no_esta:
                            print('El título no está en el catálogo... ingrese un título válido...')
                    case _:
                        print('Ingresa una opción correcta...')
            else:
                print('No hay títulos / aún no se ingresan títulos...')
        case '7':
            print('Saliendo del programa...')
            break
        case _:
            print('Elige una opción correcta...')