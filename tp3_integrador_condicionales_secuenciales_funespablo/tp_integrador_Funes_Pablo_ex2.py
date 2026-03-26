# Ejercicio 2 — “Acceso al Campus y Menú Seguro”

user = "alumno"
password = "python123"
max_intentos = 3
intentos = 0
estado_inscripcion = "Usted está INSCRIPTO"
while max_intentos > 0:
    intentos += 1
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    print(f"Intento {intentos}/3 - Usuario: {usuario} Clave: {contraseña}")
    if usuario == user and contraseña == password:
        print("Acceso concedido.")
        while True:
            print("""
1. Ver estado de inscripción
2. Cambiar clave 
3. Mostrar mensaje motivacional
4. Salir""")
            opcion = input("Elige una opción: ").strip()
            if opcion.isdigit():
                match opcion:
                    case "1":
                        print(estado_inscripcion)
                    case "2":
                        clave_nueva = input("Ingrese la clave nueva: ")
                        if len(clave_nueva) >= 6:
                            confirmacion = input("Confirma la clave: ")
                            if clave_nueva == confirmacion:
                                password = clave_nueva
                                print("Cambio realizado con éxito.")
                            else:
                                print("Confirmación incorrecta, repite la misma clave...")
                        else:
                            print("Error: mínimo 6 caracteres.")
                    case "3":
                        print('"Nadie en la breve historia de la computación ha escrito nunca un software perfecto. Es poco probable que seas el primero." Andy Hunt')
                    case "4":
                        print("Saliendo del menú...")
                        break
                    case _:
                        print("Opción fuera de rango, ingrese una opción correcta (1-4)...")
            else:
                print("Ingrese un número entero positivo...")
        break
    else:
        max_intentos -= 1
        if max_intentos == 0:
            print("Cuenta bloqueada")
        else:
            print("Contraseña o usuario incorrecto...")
            print(f"Intentos restantes: {max_intentos}")