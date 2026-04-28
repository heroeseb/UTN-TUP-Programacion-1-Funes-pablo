def pedir_nota():
    while True:
        try:
            nota = float(input('Ingrese una nota: '))
            if (0 < nota < 11):
                return nota
            else:
                print('La nota debe estar entre 1 y 10.')
        except ValueError:
            print('Ingrese un número válido')

nota_1 = pedir_nota()
nota_2 = pedir_nota()
promedio = (nota_1 + nota_2) / 2
print(f'El promedio es: {promedio}')
