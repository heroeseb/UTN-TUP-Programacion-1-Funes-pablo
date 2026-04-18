def es_entero_o_flotante(dato):
    if (dato.replace(".","").isdigit() and dato.count(".") <= 1) or isinstance(es_entero_o_flotante, (str,float)):
        return True
    else:
        return False

def input_lista_intfloat(mensaje, cantidad, condicion_opcional=None,condicion_opcional2=None):
    lista = []
    
    for _ in range(cantidad):
        while True:
            numero = input(mensaje).strip()
            
            if es_entero_o_flotante(numero):
                
                # Convertimos correctamente
                if "." in numero:
                    valor = float(numero)
                else:
                    valor = int(numero)
                
                # Validación opcional
                if condicion_opcional is not None:
                    if valor <= condicion_opcional:
                        lista.append(valor)
                        break
                    else:
                        print("El numero no cumple la condicion")
                else:
                    lista.append(valor)
                    break
            else:
                print("Ingrese un numero correcto")
    return lista


def calcular_promedio(notas):
    total = 0
    for nota in notas:
        if es_entero_o_flotante:
            total += nota
    promedio = total / len(notas)
    return promedio

def print_lista(lista):
    for elemento in lista:
        print(elemento,end=" ")
    print()

def filtrar_aprobados(notas,umbral):
    aprobado = []
    for nota in notas:
        if  nota >= umbral:
            aprobado.append(nota)
    return aprobado

def nota_maxima(notas):
    nota_max = max(notas)
    return nota_max

def nota_minima(notas):
    nota_min = min(notas)
    return nota_min

def analizar_notas(notas):
    return calcular_promedio(notas),nota_maxima(notas),nota_minima(notas)



