def validar_texto(mensaje1):
    while True:
        try:
            texto=input(mensaje1).title().strip()
            if not texto.replace(' ','').isalpha():
                raise ValueError
            return texto
        except ValueError:
            print("Error... No estás ingresando un texto válido")

def buscar_libro (lista):
    busqueda = validar_texto('Ingrese el nombre del titulo que desea buscar: ')
    encontrado = False
    for libro in lista:
        if busqueda.capitalize() == libro['titulo'].capitalize():
            encontrado = True
            print(f"Titulo: {libro['titulo']} | Copias: {libro['copias']}")
    if not encontrado:
        print('No se encontro el titulo!')

if __name__ == '__main__':
    catalogo = [
        {"titulo": "El Quijote",
        "copias": 3},
        {"titulo": "Cien Años De Soledad",
        "copias": 0}]
    buscar_libro(catalogo)




