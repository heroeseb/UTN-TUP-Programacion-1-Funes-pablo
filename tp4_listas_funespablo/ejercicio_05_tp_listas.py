
# Ejercicio 5 Agregar o quitar en una lista
alumnos = ["Laura","Diego","Lucas","Paula","Bruno","Sofia","Carla","Tomas"]
print("Los alumnos presentes son: ")
for alumno in alumnos:
    print(alumno,end=" ")
while True:
    opcion = input("\nDime si quieres agregar un nuevo estudiante (1) o eliminar uno ya existente en la lista (2) o si quieres salir del menú (0): ").strip()
    if opcion == "0":
        break
    elif opcion == "1":
        while True:
            agregar = input("Dime el nombre del alumno que quieres agregar: ").strip()
            if agregar.title() not in alumnos:
                alumnos.append(agregar.title())
                print(f"Alumno agregado: {agregar.title()}")
                break
            else:
                print("El alumno ya está en la lista")
    elif opcion == "2":
        while True:
            quitar = input("Dime el nombre del alumno que quieres quitar: ").strip()
            if quitar.title() in alumnos:
                alumnos.remove(quitar.title())
                print(f"Se eliminó al alumno {quitar.title()} de la lista correctamente")
                break
            else:
                print("Dime un nombre de alumno correcto...")
    else:
        print("Ingresa una opción válida con el número 1 o 2...")
print("La lista de alumnos actualizada es: ")
for alumno in alumnos:
    print(alumno,end=" ")