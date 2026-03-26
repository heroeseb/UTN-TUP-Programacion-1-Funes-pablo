# Ejercicio 4 — “Escape Room: La Bóveda”

# Historia
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzado_seguido = 0
bloqueo_alarma = False
print(f"--- BIENVENIDO A LA BÓVEDA ---")
while True:
    nombre_agente = input("Nombre del agente: ").strip()
    if nombre_agente.replace(" ","").isalpha():
        break
    else:
        print("Ingrese solo letras.")
print(f"-- NOMBRE DEL AGENTE: {nombre_agente.title()} --")
while True:
    if alarma == True and tiempo <= 3:
        bloqueo_alarma = True
    if cerraduras_abiertas == 3:
        print("3 cerraduras abiertas, se abrió la bóveda!!")
        print("VICTORIA!!!")
        break
    elif energia <= 0 or tiempo <= 0:
        if energia <= 0:
            print("Te quedaste sin energia!!")
            print("DERROTA!!!")
            break
        else:
            print("Te quedaste sin tiempo!!")
            print("DERROTA!!!")
            break
    elif bloqueo_alarma == True:
        print("Se bloqueo!!")
        print("DERROTA POR BLOQUEO")
        break
    print(f"CERRADURAS ABIERTA: {cerraduras_abiertas} |ENERGIA: {energia} | TIEMPO: {tiempo} | ALARMA: {'Activada' if alarma == True else 'Apagada'}")
    print("""
Menú:
1. Forzar cerradura
2. Hackear panel
3. Descansar""")
    opcion_elegida = input("Elige una acción: ").strip()
    if opcion_elegida.isdigit():
        int_opcion_elegida = int(opcion_elegida)
        if int_opcion_elegida > 0 and int_opcion_elegida <= 3:
            match opcion_elegida:
                case "1":
                    if forzado_seguido >= 2:
                        print("Se activó la alarma!!")
                        print("No abre!!")
                        print("Energía -20")
                        print("Tiempo -2")
                        alarma = True
                        energia -= 20
                        tiempo -= 2
                        forzado_seguido += 1
                    elif energia < 40:
                        print("Energía baja, hay riesgo de alarma!!")
                        while True:
                            opcion_forzar = input("Ingresa un numero del 1 al 3: ").strip()
                            if opcion_forzar.isdigit():
                                int_opcion_forzar = int(opcion_forzar)
                                if int_opcion_forzar > 0 and int_opcion_forzar <= 3:
                                    if int_opcion_forzar < 3:
                                        cerraduras_abiertas += 1
                                        energia -= 20
                                        tiempo -= 2
                                        forzado_seguido += 1
                                        print("Energía -20")
                                        print("Tiempo -2")
                                        print("Cerradura abierta!!")
                                        break
                                    else:
                                        print("Saltó la alarma!!")
                                        print("No abre la cerradura!!")
                                        print("Energía -20")
                                        print("Tiempo -2")
                                        alarma = True
                                        energia -= 20
                                        tiempo -= 2
                                        forzado_seguido += 1
                                        break
                                else:
                                    print("Ingrese una opción correcta (1 - 3).")
                            else:
                                print("Ingresa solo números...")
                    else:
                        energia -= 20
                        tiempo -= 2
                        forzado_seguido += 1
                        cerraduras_abiertas += 1
                        print("Energía -20")
                        print("Tiempo -2")
                        print("Cerradura abierta!!")
                case "2":
                    print("Comienza el Hackeo...")
                    energia -= 10
                    tiempo -= 3
                    forzado_seguido = 0
                    for i in range(4):
                        codigo_parcial += "*"
                        print(codigo_parcial + "...")
                        if len(codigo_parcial) >= 8:
                            print("Cerradura abierta!!")
                            codigo_parcial = ""
                            cerraduras_abiertas += 1
                    print("Energía -10")
                    print("Tiempo -3")
                case "3":
                    forzado_seguido = 0
                    if alarma:
                        if energia + 5 <= 100:
                            energia += 5
                            tiempo -= 1
                            print("Alarma activada!!")
                            print("Energía +5")
                            print("Tiempo -1")
                        else:
                            energia = 100
                            tiempo -= 1
                            print("Energía completa!!")
                            print("Tiempo -1")
                    else:
                        if energia + 15 <= 100:
                            energia += 15
                            tiempo -= 1
                            print("Energía +15")
                            print("Tiempo -1")
                        else:
                            energia = 100
                            tiempo -= 1
                            print("Energía completa!!")
                            print("Tiempo -1")
                    print("Has descansado!!")
                case _:
                    pass
        else:
            print("Ingrese una acción correcta (1 - 3).")
    else:
        print("Tiene que ingresar números no texto.")