# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

turno_lunes_1 = ""
turno_lunes_2 = ""
turno_lunes_3 = ""
turno_lunes_4 = ""
turno_martes_1 = ""
turno_martes_2 = ""
turno_martes_3 = ""

while True:
    nombre_operador = input("Ingrese el nombre del operador: ").strip()
    if nombre_operador.replace(" ","").isalpha():
        print(f"Hola {nombre_operador.strip()} bienvenido")
        while True:
            print("""
1. Reservar turno
2. Cancelar turno (por nombre)
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema
""")
            opcion_elegida = input("Seleccione una opción ( 1 - 5 ) : ").strip()
            if opcion_elegida.isdigit():
                if int(opcion_elegida) != 0:
                    match opcion_elegida:
                        case "1":
                            dia_reservar = input("Elegir día a reservar (1=Lunes, 2=Martes): ").strip()
                            if dia_reservar.isdigit() and (dia_reservar == "1" or dia_reservar == "2"):
                                nombre_paciente = input("Ingrese el nombre del paciente: ").strip()
                                if nombre_paciente.replace(" ","").isalpha():
                                    nombre_paciente_lower = nombre_paciente.lower()
                                    match dia_reservar:
                                        case "1":
                                            if nombre_paciente_lower == turno_lunes_1.lower() or nombre_paciente_lower == turno_lunes_2.lower() or nombre_paciente_lower == turno_lunes_3.lower() or nombre_paciente_lower == turno_lunes_4.lower():
                                                print("El paciente ya tiene un turno agendado")
                                            elif turno_lunes_1 and turno_lunes_2 and turno_lunes_3 and turno_lunes_4:
                                                print("Agenda de turnos de día Lunes completa...")
                                            else:
                                                for i in range(4):
                                                    match i:
                                                        case 0:
                                                            if turno_lunes_1 == "":
                                                                turno_lunes_1 = nombre_paciente.title()
                                                                print("Turno registrado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case 1:
                                                            if turno_lunes_2 == "":
                                                                turno_lunes_2 = nombre_paciente.title()
                                                                print("Turno registrado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case 2:
                                                            if turno_lunes_3 == "":
                                                                turno_lunes_3 = nombre_paciente.title()
                                                                print("Turno registrado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case 3:
                                                            if turno_lunes_4 == "":
                                                                turno_lunes_4 = nombre_paciente.title()
                                                                print("Turno registrado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                        case "2":
                                            if nombre_paciente_lower == turno_martes_1.lower() or nombre_paciente_lower == turno_martes_2.lower() or nombre_paciente_lower == turno_martes_3.lower():
                                                print("El paciente ya tiene un turno agendado")
                                            elif turno_martes_1 and turno_martes_2 and turno_martes_3:
                                                print("Agenda de turnos de día Martes completa...")
                                            else:
                                                for i in range(3):
                                                    match i:
                                                        case 0:
                                                            if turno_martes_1 == "":
                                                                turno_martes_1 = nombre_paciente.title()
                                                                print("Turno registrado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case 1:
                                                            if turno_martes_2 == "":
                                                                turno_martes_2 = nombre_paciente.title()
                                                                print("Turno registrado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case 2:
                                                            if turno_martes_3 == "":
                                                                turno_martes_3 = nombre_paciente.title()
                                                                print("Turno registrado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                else:
                                    print("Ingrese una opcion válida")
                            else:
                                print("Ingrese una opcion válida")
                        case "2":
                            dia_cancelar = input("Elegir día para cancelar turno (1=Lunes, 2=Martes): ").strip()
                            if dia_cancelar.isdigit() and (dia_cancelar == "1" or dia_cancelar == "2"):
                                nombre_paciente = input("Ingrese el nombre del paciente: ").strip()
                                if nombre_paciente.replace(" ","").isalpha():
                                    nombre_paciente_lower = nombre_paciente.lower()
                                    match dia_cancelar:
                                        case "1":
                                            if not turno_lunes_1 and not turno_lunes_2 and not turno_lunes_3 and not turno_lunes_4:
                                                print("Agenda de turnos de día Lunes vacia...")
                                            else:
                                                for i in range(4):
                                                    match i:
                                                        case 0:
                                                            if turno_lunes_1.lower() == nombre_paciente_lower:
                                                                turno_lunes_1 = ""
                                                                print("Turno cancelado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case 1:
                                                            if turno_lunes_2.lower() == nombre_paciente_lower:
                                                                turno_lunes_2 = ""
                                                                print("Turno cancelado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case 2:
                                                            if turno_lunes_3.lower() == nombre_paciente_lower:
                                                                turno_lunes_3 = ""
                                                                print("Turno cancelado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case 3:
                                                            if turno_lunes_4.lower() == nombre_paciente_lower:
                                                                turno_lunes_4 = ""
                                                                print("Turno cancelado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case _:
                                                            print(f"El paciente {nombre_paciente.title()} no está en la lista")
                                        case "2":
                                            if not turno_martes_1 and not turno_martes_2 and not turno_martes_3:
                                                print("Agenda de turnos de día martes vacia...")
                                            else:
                                                for i in range(4):
                                                    match i:
                                                        case 0:
                                                            if turno_martes_1.lower() == nombre_paciente_lower:
                                                                turno_martes_1 = ""
                                                                print("Turno cancelado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case 1:
                                                            if turno_martes_2.lower() == nombre_paciente_lower:
                                                                turno_martes_2 = ""
                                                                print("Turno cancelado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case 2:
                                                            if turno_martes_3.lower() == nombre_paciente_lower:
                                                                turno_martes_3 = ""
                                                                print("Turno cancelado con éxito!!")
                                                                break
                                                            else:
                                                                continue
                                                        case _:
                                                            print(f"El paciente {nombre_paciente.title()} no está en la lista")
                                else:
                                    print("Ingrese una opción válida")
                            else:
                                print("Ingrese una opción válida...")
                        case "3":
                            print("Turnos día Lunes: ")
                            if turno_lunes_1:
                                print(f"Turno 1: paciente {turno_lunes_1}")
                            else:
                                print("Libre")
                            if turno_lunes_2:
                                print(f"Turno 2: paciente {turno_lunes_2}")
                            else:
                                print("Libre")
                            if turno_lunes_3:
                                print(f"Turno 3: paciente {turno_lunes_3}")
                            else:
                                print("Libre")
                            if turno_lunes_4:
                                print(f"Turno 4: paciente {turno_lunes_4}")
                            else:
                                print("Libre")
                            print("Turnos día Martes: ")
                            if turno_martes_1:
                                print(f"Turno 1: paciente {turno_martes_1}")
                            else:
                                    print("Libre")
                            if turno_martes_2:
                                print(f"Turno 2: paciente {turno_martes_2}")
                            else:
                                print("Libre")
                            if turno_martes_3:
                                print(f"Turno 3: paciente {turno_martes_3}")
                            else:
                                print("Libre")
                        case "4":
                            cant_turnos_dia1 = 0
                            cant_turnos_dia2 = 0
                            for i in range(7):
                                match i:
                                    case 0:
                                        if turno_lunes_1:
                                            cant_turnos_dia1 += 1
                                        else:
                                            continue
                                    case 1:
                                        if turno_lunes_2:
                                            cant_turnos_dia1 += 1
                                        else:
                                            continue
                                    case 2:
                                        if turno_lunes_3:
                                            cant_turnos_dia1 += 1
                                        else:
                                            continue
                                    case 3:
                                        if turno_lunes_4:
                                            cant_turnos_dia1 += 1
                                        else:
                                            continue
                                    case 4:
                                        if turno_martes_1:
                                            cant_turnos_dia2 += 1
                                        else:
                                            continue
                                    case 5:
                                        if turno_martes_2:
                                            cant_turnos_dia2 += 1
                                        else:
                                            continue
                                    case 6:
                                        if turno_martes_3:
                                            cant_turnos_dia2 += 1
                                        else:
                                            continue
                            print(f"""
Turnos ocupados día Lunes: {cant_turnos_dia1}
Turnos disponibles día Lunes: {4 - cant_turnos_dia1}
Turnos ocupados día Martes: {cant_turnos_dia2}
Turnos disponibles día Martes: {3 - cant_turnos_dia2}
""")
                            if cant_turnos_dia1 == cant_turnos_dia2:
                                print("Día con mas turnos: Empate")
                            elif cant_turnos_dia1 > cant_turnos_dia2:
                                print("Día con mas turnos: Lunes")
                            else:
                                print("Día con mas turnos: Martes")
                        case "5":
                            print("Cerrando sistema...")
                            break
                        case _:
                            print("Ingrese una opción válida (1-5)")
            else:
                print("Ingrese una opción correcta, solo números...")
        break
    else:
        print("Ingrese un nombre correcto...")