from funciones.funciones_3 import *

while True:
    print('1. Celsius → Fahrenheit' )
    print('2. Fahrenheit → Celsius')
    print('3. Salir')
    opcion = input_int('Ingrese una opción: ','Ingrese un numero correcto!')
    match opcion:
        case 1:
            temperatura = input_float('Ingrese la temperatura a convertir(Celcius): ','Ingrese un numero correcto')
            temp_convertido = celsius_a_fahrenheit(temperatura)
            print(f'Resultado Celsius → Fahrenheit: {temp_convertido:.2f}')
        case 2:
            temperatura = input_float('Ingrese la temperatura a convertir(Farenheit): ','Ingrese un numero correcto')
            temp_convertido = fahrenheit_a_celsius(temperatura)
            print(f'Resultado Fahrenheit → Celsius: {temp_convertido:.2f}')
        case 3:
            print('Saliendo del programa!...')
            break
        case _:
            print('Ingrese una opción correcta!')