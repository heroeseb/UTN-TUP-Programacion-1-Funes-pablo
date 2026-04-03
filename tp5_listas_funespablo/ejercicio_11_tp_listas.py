# Crear una lista con los nombres de 10 estudiantes.
# ● Solicitar al usuario que ingrese un nombre a buscar.
# ● Indicar si el nombre se encuentra en la lista.
# ● Mostrar la posición en la que aparece.
# ● Si no se encuentra, informar que no está en la lista.

lista = ["Sebastian","Pablo","Juan","Micaela","Roberto","Santiago","Lucas","Erika","Marcelo","Alejandra"]
print("La lista de estudiantes es: ")
for alumno in lista:
    print(alumno,end=" ")
while True:
    nombre = input("\nIngrese un nombre a buscar: ").strip()
    if nombre.replace(" ","").isalpha():
        nombre_title = nombre.title()
        if nombre_title in lista:
            print(f"El nombre {nombre_title} se encuentra en la lista")
            indice_nombre = lista.index(nombre_title)
            print(f"Se encuentra en la posición {indice_nombre + 1}")# le agrego un +1 porque no se si se debe mostrar la posicion a partir del 0 o del 1 asi que asumo que es a partir del 1
            break
        else:
            print("No se encuentra en la lista")
    else:
        print("Ingrese un nombre válido")