habitaciones=[284, 305, 310]
estados=[0, 1, 0]

while True:
    print("""Menú:
        1.Ingresar números de habitación: (Registrar las habitaciones del hotel)
        2.Ingresar estados (0/1) paralelos: (Definir el estado inicial de cada habitación)
        3.Mostrar estado general: (Mostrar el estado de todas las habitaciones)
        4.Consultar estado de una habitación: (Verificar el estado de una habitación específica)
        5.Listar ocupadas o libres (según lo que se pida): (Mostrar una lista de habitaciones según su estado)
        oPermite al usuario elegir si quiere ver la lista de habitaciones ocupadas o la lista de habitaciones libres.
        6.Agregar habitación: (Añadir una nueva habitación al sistema)
        oPermite al usuario agregar una nueva habitación al sistema, asignándole un estado inicial (libre u ocupada).
        7.Cambiar estado: (Cambiar el estado de una habitación)
        oPermite al usuario cambiar el estado de una habitación (de libre a ocupada o de ocupada a libre). Debe solicitar el número de habitación y el nuevo estado deseado.
        8.Salir: (Terminar el programa)""")
    opcion = input("Ingrese una opción: ")
    match opcion:
        case 1:
            while True:
                habitacion = input("Ingrese numero de habitación habitación (si ingresa 0 se termina): ")
                