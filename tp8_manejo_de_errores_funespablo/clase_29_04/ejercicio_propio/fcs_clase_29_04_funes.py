import copy


class ErrorHabitacionDuplicada(Exception):
    pass
class ErrorNumeroNegativo(Exception):
    pass


def validar_input_numero(mensaje,mensaje_2):
    try:
        input1 = int(input(mensaje))
        if input1 < 0:
            raise ErrorNumeroNegativo('Ingrese un numero positivo')
        return input1
    except ValueError:
        print(mensaje_2)
    except ErrorNumeroNegativo as e:
        print(e)

def comparar_valor (dato, condicion,mensaje=None):
    if dato == condicion:
        return True
    else:
        if mensaje:
            print(mensaje)
        return False


def caso_1(lista):
    copia_lista = copy.deepcopy(lista)
    habitacion_input = validar_input_numero('Ingrese el numero de habitacion: ','Ingrese un numero valido')
    while not habitacion_input:
        habitacion_input = validar_input_numero('Ingrese el numero de habitacion: ','Ingrese un numero valido')
    try:
        for habitacion in copia_lista:
            if habitacion['numero'] == habitacion_input:
                raise ErrorHabitacionDuplicada('La habitacion ya esta cargada')
    except ErrorHabitacionDuplicada as e:
        print(e)
        return copia_lista
    else:
        estado_input = validar_input_numero('Ingrese el estado de la habitación: ','Ingrese un numero válido!')
        while estado_input not in (0, 1):
            print('Ingrese 1 (ocupado) o 0 (libre)...')
            estado_input = validar_input_numero('Ingrese el estado de la habitación: ','Ingrese un numero válido!')
        diccionario = {'numero' : habitacion_input, 'estado' : estado_input}
        copia_lista.append(diccionario)
        print('Habitación cargada con exito!')
        return copia_lista

def caso_2(lista):
    for elemento in lista:
        print(f'Habitación: {elemento["numero"]} {"Ocupada" if elemento["estado"] == 1 else "Libre" }')

def caso_3(lista):
    bandera = True
    habitacion = validar_input_numero('Ingrese el numero de la habitación que desea consultar: ','Ingrese un numero correcto')
    for hab in lista:
        if hab['numero'] == habitacion:
            print(f'Habitación: {hab["numero"]} {"Ocupada" if hab["estado"] == 1 else "Libre" }')
            bandera = False
            break
    if bandera and habitacion:
        print('No esta cargada esa habitación')

def caso_4(lista):
    copia_lista = copy.deepcopy(lista)
    bandera = True
    habitacion = validar_input_numero('Ingrese el numero de la habitación que desea consultar: ','Ingrese un numero correcto')
    for hab in copia_lista:
        if hab['numero'] == habitacion:
            bandera = False
            print(f'El estado de la habitacion {hab['numero']} es : {'Ocupado' if hab['estado'] == 1 else 'Libre'}')
            nuevo_estado = validar_input_numero('Cual es el nuevo estado que le quieres asignar a la habitacion (1 ocupado o 0 libre): ','Ingrese un numero correcto!')
            while nuevo_estado not in (0,1):
                print('Ingrese una opcion correcta (1 o 2)...')
                nuevo_estado = validar_input_numero('Cual es el nuevo estado que le quieres asignar a la habitacion (1 ocupado o 0 libre): ','Ingrese un numero correcto!')
            hab['estado'] = nuevo_estado
            print('Estado cambiado con exito!')
            break
    if bandera and habitacion:
        print('No esta cargada esa habitación')
    return copia_lista

def caso_5(lista):
    while True:
        opcion = validar_input_numero('Ingrese si quiere listar habitaciones libres(1) u ocupadas(2): ','Ingrese un número correcto')
        match opcion:
            case 1:
                for habitacion in lista:
                    if habitacion['estado'] == 0:
                        print(f'Habitación {habitacion["numero"]} libre')
                break
            case 2:
                for habitacion in lista:
                    if habitacion['estado'] == 1:
                        print(f'Habitación {habitacion["numero"]} Ocupada')
                break
            case _:
                print('Ingrese una opcion dentro del rango (1 o 2)')


if __name__ == '__main__':
    habitaciones = [{
        "numero": 101,
        "estado": 0 # 0 = libre, 1 = ocupada
    },
    {
        "numero": 102,
        "estado": 1 # 0 = libre, 1 = ocupada
    }]
