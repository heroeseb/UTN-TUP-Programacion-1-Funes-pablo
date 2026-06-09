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

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique.

def fibo(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibo(numero - 1) + fibo(numero - 2)

def mostrar_fibo():
    try:
        print('Se mostrara la serie completa de Fibonacci hasta la posición que indique')
        cantidad = int(input('Ingrese la posición: '))
        for i in range(cantidad + 1):
            print(fibo(i),end=' ')
    except ValueError:
        print('Ingrese un numero correcto')

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1)
# . Prueba esta función en un 
# algoritmo general.

def potencia(n,m):
    if m == 0:
        return 1
    return n * potencia(n,m - 1)

def mostrar_potencia():
    try:
        base = int(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        if exponente < 0:
            raise ValueError
        resultado = potencia(base, exponente)
        print(f"{base}^{exponente} = {resultado}")
    except ValueError:
        print('Ingrese un numero correcto!')

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este 
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0 
# 5 ÷ 2 = 2 resto: 1 
# 2 ÷ 2 = 1 resto: 0 
# 1 ÷ 2 = 0 resto: 1 
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

def binario(num):
    if num < 2:
        return str(num)
    cociente = num // 2
    resto = num % 2
    return binario(cociente) + str(resto)

def convertir_numero_binario():
    try:
        num = int(input('Ingrese el número que desea convertir a binario: '))
        if num < 0:
            raise ValueError
        print(f'El numero {num} en binario es: {binario(num)}')
    except ValueError:
        print('Ingrese un número correcto!')

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

def mostrar_es_p():
    try:
        palabra = input('Ingrese una palabra: ')
        if not palabra:
            raise ValueError
        print(f'La palabra {palabra} {'es palindromo' if es_palindromo(palabra) else 'no es palindromo'}')
    except ValueError:
        print('Ingrese una palabra correcta!')

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    return suma_digitos(n % 10) + suma_digitos(n // 10) 

def pedir_numero_sumar():
    try:
        num = int(input('Ingrese un número: '))
        if num < 0:
            raise ValueError
        print(f'La suma de los digitos del número {num} es {suma_digitos(num)}')
    except ValueError:
        print('Ingrese un número correcto!')

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

def input_contar_bloques():
    try:
        niveles = int(input('Ingrese la cantidad de bloques del nivel inferior: '))
        if niveles < 1:
            raise ValueError
        print(f'Total de bloques necesarios: {contar_bloques(niveles)}')
    except ValueError:
        print('Ingrese un número correcto!')

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3 
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

def pedir_num_contar():
    try:
        numero = int(input('Ingrese un número entero positivo: '))
        if numero < 0:
            raise ValueError('El número debe ser positivo')
        digito = int(input('Ingrese el dígito a buscar (0-9): '))
        if digito < 0 or digito > 9:
            raise ValueError('El dígito debe estar entre 0 y 9')
        cantidad = contar_digito(numero, digito)
        print(f'El dígito {digito} aparece {cantidad} veces en el número {numero}')
    except ValueError:
        print('Ingrese un numero correcto!')

if __name__ == '__main__':
    print('Ejercicio 1')
    input_factorial()
    print('Ejercicio 2')
    mostrar_fibo()
    print('Ejercicio 3')
    mostrar_potencia()
    print('Ejercicio 4')
    convertir_numero_binario()
    print('Ejercicio 5')
    mostrar_es_p()
    print('Ejercicio 6')
    pedir_numero_sumar()
    print('Ejercicio 7')
    input_contar_bloques()
    print('Ejercicio 8')
    pedir_num_contar()