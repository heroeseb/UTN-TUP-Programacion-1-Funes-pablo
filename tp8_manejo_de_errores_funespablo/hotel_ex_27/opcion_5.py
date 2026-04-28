def habitaciones_libres_ocupadas(diccionario):
    while True:
        try:
            opcion = int(input('Ingrese si quiere listar habitaciones libres(1) u ocupadas(2): ').strip())
        except ValueError:
            print('Ingrese un número correcto')
        else:
            match opcion:
                case 1:
                    for habitacion in diccionario:
                        if habitacion['estado'] == 0:
                            print(f'Habitación {habitacion['numero']} libre')
                    break
                case 2:
                    for habitacion in diccionario:
                        if habitacion['estado'] == 1:
                            print(f'Habitación {habitacion['numero']} Ocupada')
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

habitaciones_libres_ocupadas(habitaciones)