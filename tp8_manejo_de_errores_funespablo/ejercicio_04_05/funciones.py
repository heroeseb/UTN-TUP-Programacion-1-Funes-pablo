def validar_texto(mensaje_1,mensaje_2):
    while True:
        try:
            texto = input(mensaje_1).strip()
            if texto.isalpha():
                print(mensaje_2)
                return texto
            else:
                print("ERROR... El texto solo puede contener letras.")
        except KeyboardInterrupt:
            print("Se interrumpió el programa por el usuario.")
            break
        except Exception as e:
            print(f"Hubo un error inesperado... Error: {e}.")
def validar_entero(mensaje_1,mensaje_2):
    while True:
        try:
            numero = int(input(mensaje_1))
            if numero < 0:
                print("ERROR... No se permiten números negativos.")
                continue
            print(mensaje_2)
            return numero
        except ValueError:
            print("ERROR... Por favor ingrese un número entero.")
        except Exception as e:
            print(f"Hubo un error inesperado... Error: {e}.")
def validar_entero(mensaje_1,mensaje_2):
    while True:
        try:
            numero = float(input(mensaje_1))
            if numero < 0:
                print("ERROR... No se permiten números negativos.")
                continue
            print(mensaje_2)
            return numero
        except ValueError:
            print("ERROR... Por favor ingrese un número entero.")
        except Exception as e:
            print(f"Hubo un error inesperado... Error: {e}.")



def mostrar_menu():
    print('''\n---Menu---
1. Agregar pais
2. Listar paises
3. Buscar pais
4. Modificar pais
5. Eliminar
6. Salir''')
    
def agregar_pais(paises):
    nombre = input('Ingrese el nombre del pais: ')
    poblacion = int(input('Ingrese la poblacion del pais: '))
    superficie = float(input('Ingrese la superficie del pais: '))
    continente = input('Ingrese el continente del pais: ')

    pais_nvo = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente' : continente
    }

    paises.append(pais_nvo)
    print('Pais agregado correctamente.')
    return paises

def listar_paises(paises):
    if not paises:
        print('No hay paises que mostrar.')
    else:
        for pais in paises:
            print()
            for k,v in pais.items():
                print(f'{k}: {v}')

def buscar_pais(paises):
    if not paises:
        print('No hay paises cargados.')
    else:
        nombre_pais = input('Ingrese el pais a buscar: ')
        encontrado = False
        for pais in paises:
            if nombre_pais == pais['nombre']:
                print(f'Pais encontrado: {pais}')
                encontrado = True
        if not encontrado:
            print('Pais no encontrado.')

def modificar_pais(paises):
    if not paises:
        print('No hay paises cargados.')
    else:
        nombre_pais = input('Ingrese el pais a modificar: ')
        encontrado = False
        for pais in paises:
            if nombre_pais == pais['nombre']:
                print(f'Pais encontrado: {pais}')
                encontrado = True

                pais['poblacion'] = int(input(f'Ingrese la nueva poblacion para {pais['nombre']}: '))
                pais['superficie'] = float(input(f'Ingrese la nueva superficie para {pais['nombre']}: '))
                print('Pais modificado')

        if not encontrado:
            print('Pais no encontrado.')
        
    return paises

def eliminar_pais(paises):
    if not paises:
        print('No hay paises cargados.')
    else:
        nombre_pais = input('Ingrese el pais a eliminar: ')
        encontrado = False
        for pais in paises:
            if nombre_pais == pais['nombre']:
                print(f'Pais encontrado')
                encontrado = True
                paises.remove(pais)
                print('Pais eliminado.')

    if not encontrado:
            print('Pais no encontrado.')
    
    return paises