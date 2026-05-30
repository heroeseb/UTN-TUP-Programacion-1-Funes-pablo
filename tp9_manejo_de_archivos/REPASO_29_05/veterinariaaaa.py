



def input_str(mensaje,mensaje_error):
    try:
        dato = input(mensaje).strip()
        if not dato.replace(' ','').isalpha():
            raise ValueError
        return dato.title()
    except ValueError :
        print(f'Error: {mensaje_error}')

def input_int(mensaje,mensaje_error):
    try:
        dato = int(input(mensaje))
        if dato < 0:
            raise ValueError
        return dato
    except ValueError:
        print(mensaje_error)



def registrar_mascotas(pacientes):
    if not pacientes:
        cant_registros = input_int('Ingrese la cantidad de mascotas que se van a registrar: ','Ingrese un numero correcto')
        while not cant_registros:
            cant_registros = input_int('Ingrese la cantidad de mascotas que se van a registrar: ','Ingrese un numero correcto')
        for _ in range(cant_registros):
            while True:
                nueva_mascota = alta_mascota(pacientes)
                if nueva_mascota:
                    pacientes.append(nueva_mascota)
                    break
        return pacientes
    else:
        print('Para agregar nuevas mascotas debe usarse la opción 5')
        return pacientes



def mostrar_pacientes(pacientes):
    if not pacientes:
        print('La lista no ha sido inicializada')
        return
    for mascota in pacientes:
        print(f'Nombre: {mascota['mascota']} Turnos pendientes actuales: {mascota['turnos']}')


def consultar_turnos(pacientes):
    if not pacientes:
        print('La lista no ha sido inicializada')
        return
    consulta = input_str('Ingrese el nombre de la mascota a consultar turnos: ','Ingrese un nombre valido')
    if not consulta:
        return
    for mascota in pacientes:
        if consulta.title() == mascota['mascota'].title():
            print(f'{mascota['mascota']} tiene {mascota['turnos']} turnos pendientes registrados')
            return
    print('No se encontro el nombre en la lista')


def reporte_sin_turnos(pacientes):
    if not pacientes:
        print('La lista no ha sido inicializada')
        return
    encontrado = False
    for mascota in pacientes:
        if mascota['turnos'] == 0:
            if not encontrado:
                print('Reporte de mascotas sin turnos:')
            encontrado = True
            print(f'{mascota['mascota']} ya completo toda su atencion o aun no tienen turno asignado')
    if not encontrado:
        print('No hay mascotas sin turnos')



def alta_mascota(pacientes):
    nombre_mascota = input_str('Ingrese el nombre de la mascota: ','Ingrese un nombre correcto')
    if nombre_mascota == None:
        return 
    if not nombre_mascota.title() in [p['mascota'].title() for p in pacientes]:
        turnos = input_int(f'Ingrese la cantidad de turnos para {nombre_mascota}: ','Ingrese un numero correcto!')
        if turnos == None:
            return 
        pacientes_dicc = {'mascota':nombre_mascota,'turnos':turnos}
        print(f'Se registro con exito {nombre_mascota.title()}')
        return pacientes_dicc
    print('La mascota ya esta registrada')
    return

def actualizar_turnos(pacientes):
    if not pacientes:
        print('La lista aun no ha sido inicializada')
        return pacientes
    nombre_mascota = input_str('Ingrese el nombre de la mascota: ','Ingrese un nombre correcto!')
    if not nombre_mascota:
        return pacientes
    for mascota in pacientes:
        if nombre_mascota == mascota['mascota']:
            print('''
                1. Atención
                2. Asignación
                ''')
            opcion = input_int('Ingrese una opcion: ','Ingresa un numero correcto!')
            match opcion:
                case 1:
                    if not (mascota['turnos'] > 0):
                        print('No tiene turnos asignados')
                        return pacientes
                    mascota['turnos'] -= 1
                    print('Turno modificado exitosamente!')
                    return pacientes
                case 2:
                    mascota['turnos'] += 1
                    print('Turno modificado exitosamente!')
                    return pacientes
    print('No se encontro la mascota!')
    return pacientes

# Bloque principal
pacientes = [{'mascota':'Benja','turnos':0},{'mascota':'Capullo','turnos':0}]
# pacientes = []
opcion = 0
while True:
    try:
        print('''
            1. Registro Inicial de Mascotas
            2. Visualizacion de Pacientes
            3. Consulta de Turnos
            4. Reporte de Mascotas sin Turnos
            5. Alta de Nueva Mascota
            6. Actualizacion de Turnos (Asignacion / Atencion)
            7. Salir
            ''')
        opcion = int(input('Seleccione una opcion: '))
        match opcion:
            case 1:
                pacientes = registrar_mascotas(pacientes)
            case 2:
                mostrar_pacientes(pacientes)
            case 3:
                consultar_turnos(pacientes)
            case 4:
                reporte_sin_turnos(pacientes)
            case 5:
                paciente_nuevo = alta_mascota(pacientes)
                if paciente_nuevo != None:
                    pacientes.append(paciente_nuevo)
            case 6:
                pacientes = actualizar_turnos(pacientes)
            case 7:
                print('Saliendo del programa!')
                break
            case _:
                print('Ingrese una opción correcta!')
    
    except ValueError:
        print(f'Error: Ingrese un numero correcto!')
