from funciones import mostrar_inventario,cantidad_a_ingresar, solicita_nombre_herramienta,validar_duplicado

def main():
    inventario=[{"herramienta":"pala"
             ,"cantidad":3}]    
    while True:
        print('''
            Bienvenido a la Ferreteria de Ariel
            1) Ingresar Herramientas
            2)Ingresar Cantidades
            3)Mostrar
            4) Salir
            ''')
        opcion=input("Ingrese la opcion deseada: ")
        
        match opcion:
            case "1":
                cantidad=cantidad_a_ingresar("Ingrese el numero de herramientas a cargar: ","El valor ingresado no es valido, intente de nuevo")
                for i in range(cantidad):
                    herramienta=solicita_nombre_herramienta()
                    while validar_duplicado(herramienta,inventario):
                        herramienta=solicita_nombre_herramienta()
                    inventario.append({"herramienta":herramienta,
                                       "cantidad":0})
                
            case "2":
                cantidad=cantidad_a_ingresar("Ingrese el numero de stock a cargar: ","El valor ingresado no es valido, intente de nuevo")
            case "3":
                mostrar_inventario(inventario)
            case "4":
                print("Gracias por visitarnos. Adios")
                break
            case _:
                print("La opcion ingresada no es valida")

if __name__=="__main__":
    main()