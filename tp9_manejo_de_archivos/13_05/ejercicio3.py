def celsius_a_fahrenheit(temp):
    farenheit = (temp * 9/5) + 32
    return farenheit

def fahrenheit_a_celsius(temp):
    celcius = (temp - 32) * 5/9
    return celcius

def input_int(mensaje,mensaje2):
    while True:
        try:
            input_salida = int(input(mensaje))
            return input_salida
        except ValueError:
            print(mensaje2)

def input_float(mensaje,mensaje2):
    while True:
        try:
            input_salida = float(input(mensaje))
            return input_salida
        except ValueError:
            print(mensaje2)

def main3():
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


main3()