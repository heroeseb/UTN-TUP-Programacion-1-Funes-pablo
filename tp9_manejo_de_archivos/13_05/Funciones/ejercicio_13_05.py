def calcular_promedio(lista):
    if not lista:
        print('La lista se encuentra vacia.')
        return 0
    
    promedio = sum(lista) / len(lista)
    return promedio

