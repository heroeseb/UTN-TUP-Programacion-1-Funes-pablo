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