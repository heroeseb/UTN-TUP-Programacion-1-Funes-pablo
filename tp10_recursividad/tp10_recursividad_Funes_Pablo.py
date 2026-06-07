# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial (numero):
    if numero == 1:
        return 1
    elif numero < 0:
        return
    return numero * factorial(numero - 1)

def input_factorial():
    try:
        print('Se calculara el factorial de todos los números enteros entre 1 y el número que indique')
        num = int(input('Ingrese el numero: '))
        if num < 1:
            raise ValueError
        for i in range(1,num+1):
            print(factorial(i))
    except ValueError:
        print('Ingrese un número correcto!')

input_factorial()
