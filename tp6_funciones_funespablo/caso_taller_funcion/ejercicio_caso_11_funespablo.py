# Funes Pablo Sebastian
from funciones import *
ordenes= ["ORD-001", "ORD-002", "ORD-003"]
horas= [2.5, 0, 4.0]
# horas= [2.5]

while True:
    mostrar_menu()
    opcion = input("Elija una opción: ").strip()
    match opcion:
        case "1":
            ordenes,horas = caso_1(ordenes,horas)
        case "2":
            ordenes,horas = caso2(ordenes,horas)
        case "3":
            caso3(ordenes,horas)
        case "4":
            caso4(ordenes,horas)
        case "5":
            caso5(ordenes,horas)
        case "6":
            ordenes,horas = caso6(ordenes,horas)
        case "7":
            ordenes,horas = caso7(ordenes,horas)
        case "8":
            print("Saliendo del programa")
            break
        case _:
            print("Elija una opción correcta...")





