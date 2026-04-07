import random

palabras = [
    "python",
    "variable",
    "funcion",
    "bucle",
    "condicional",
    "algoritmo",
    "computadora",
    "programacion",
    "desarrollo",
    "software",
    "hardware",
    "internet",
    "servidor",
    "cliente",
    "base",
    "datos",
    "codigo",
    "debug",
    "compilar",
    "ejecutar",
    "archivo",
    "sistema",
    "red",
    "seguridad",
    "inteligencia",
    "artificial",
    "teclado",
    "pantalla",
    "memoria"
]
def elegir_palabra(lista):
    palabra_aleatorio = random.choice(lista)
    return palabra_aleatorio
palabra_elegida = elegir_palabra(palabras)
letras_acertadas = []


def ingresa_letra():
    while True:
        letra = input("Ingrese una letra: ").strip()
        if letra.isalpha():
            return letra.lower()
numero_intentos = 6
def mostrar_tablero(lista):
    for letra in lista:
        if letra.lower() in letras_acertadas:
            print(letra,end=" ")
        else:
            print("_",end=" ")
    print("\n")
def letra_esta(letra):
    if letra in palabra_elegida:
        letras_acertadas.append(letra.lower())
        print("Adivinaste una letra correctamente!")
        return True
    else:
        print(f"Letra incorrecta, te quedan {numero_intentos-1} intentos")
        return False

todas_las_letras = False
while True:
    mostrar_tablero(palabra_elegida)

    if todas_las_letras:
        print("Ganaste!!")
        break
    elif numero_intentos <= 0:
        print("Perdiste!!")
        break
    letra_ingresada = ingresa_letra()
    letraestaria = letra_esta(letra_ingresada)
    
    if not letraestaria:
        numero_intentos -= 1
    for letra in palabra_elegida:
        if letra in letras_acertadas:
            todas_las_letras = True
        else:
            todas_las_letras = False
            break
