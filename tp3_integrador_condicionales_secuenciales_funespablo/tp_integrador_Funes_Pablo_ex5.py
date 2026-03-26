#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
dano_base_ataque_pesado = 15
dano_base_enemigo = 12
turno_gladiador = True
primer_turno = True
print("--- BIENVENIDO A LA ARENA ---")
while True:
    nombre_gladiador = input("Nombre del Gladiador: ").strip()
    if nombre_gladiador.replace(" ","").isalpha():
        print(f"Nombre del Gladiador: {nombre_gladiador.title()}")
        print("=== INICIO DEL COMBATE ===")
        while vida_gladiador > 0 and vida_enemigo > 0:
            if turno_gladiador:
                if primer_turno:
                    print(f"{nombre_gladiador.title()} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")
                    primer_turno = False
                else:
                    print("=== NUEVO TURNO ===")
                    print(f"{nombre_gladiador.title()} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")
                while True:
                    print("""
Elige una acción: 
1. Ataque Pesado 
2. Ráfaga Veloz 
3. Curar""")
                    opcion_elegida = input("Opción: ").strip()
                    if opcion_elegida.isdigit():
                        int_opcion_elegida = int(opcion_elegida)
                        match int_opcion_elegida:
                            case 1:
                                if vida_enemigo < 20:
                                    golpe_critico = dano_base_ataque_pesado * 1.5
                                    vida_enemigo = 0 # si le resto el calculo de {golpe_critico} la variable utilizada para la vida del enemigo se "convertiria" en un float, por esta razon, y como de todas formas al tener menos de 20 puntos de vida la vida quedaria en 0 preferi asignarle ese valor directamente a la variable
                                    print(f">>¡Atacaste al enemigo por {golpe_critico} puntos de daño!")
                                    print(">>¡Puntos de vida del enemigo disminuidos a 0!")
                                    break
                                else:
                                    vida_enemigo -= dano_base_ataque_pesado
                                    turno_gladiador = False
                                    print(f">>¡Atacaste al enemigo por {dano_base_ataque_pesado} puntos de daño!")
                                    break
                            case 2:
                                turno_gladiador = False
                                print(">> ¡Inicias una ráfaga de golpes!")
                                for i in range(3):
                                    vida_enemigo -= 5
                                    print("> Golpe conectado por 5 de daño")
                                break
                            case 3:
                                if pociones_vida > 0:
                                    vida_gladiador += 30
                                    pociones_vida -= 1
                                    turno_gladiador = False
                                    print(">> +30 puntos de vida")
                                    break
                                else:
                                    print(">>¡No quedan pociones!")
                                    turno_gladiador = False
                                    break
                            case _:
                                print("Error: Ingrese un número válido. (1-3)")
                    else:
                        print("Error: Ingrese un número.")
            else:
                vida_gladiador -= dano_base_enemigo
                print(f">>¡El enemigo te atacó por {dano_base_enemigo} puntos de daño!")
                turno_gladiador = True
    else:
        print("Error: Solo se permiten letras")
    if vida_gladiador > 0:
        print(f"¡VICTORIA! {nombre_gladiador.title()} ha ganado la batalla.")
    elif vida_gladiador <= 0:
        print("DERROTA. Has caído en combate")
    break

