def mostrar_inventario(lista):
    '''
    Recibe una lista de diccionarios y los imprime
    por consola
    '''
    for herramienta in lista:
        print(f"De la herramienta {herramienta["herramienta"]} tenemos {herramienta["cantidad"]} en existencias")
 
def cantidad_a_ingresar(mensaje,mensaje_fallido):
    '''Solicita ingresar un numero positivo
    distinto de 0
    ''' 
    cantidad=input(mensaje)
    while not cantidad.isdigit() or cantidad=="0":
        print(mensaje_fallido)
        cantidad=input(mensaje)
    cantidad_int=int(cantidad)
    return cantidad_int

def solicita_nombre_herramienta():
    '''Solicita ingresar un nombre de herramienta valido
    ''' 
    herramienta=input("Ingrese el nombre de la herramientas a cargar: ").strip().lower()
    while not herramienta.isalpha():
        print("El valor ingresado no es valido, intente de nuevo")
        herramienta=input("Ingrese el nombre de la herramientas a cargar: ").strip().lower()
    
    return herramienta



def validar_duplicado(nombre_buscado,lista):
    for herramienta in lista:
        if herramienta["herramienta"]==nombre_buscado:
            print(f"La herramienta {nombre_buscado} ya existe en el inventario")
            return True
    return False
    


if __name__=="__main__":
    lista=[{"herramienta":"Destornillador",
            "cantidad":3},
           {"herramienta":"Cinta metrica",
            "cantidad":4}]
    mostrar_inventario(lista)