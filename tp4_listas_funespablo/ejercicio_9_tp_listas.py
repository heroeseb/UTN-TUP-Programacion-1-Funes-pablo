
# Ejercicio 9 Ta-te-ti
tablero = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]
contador = 0
while True:
    if (tablero[0][0] == tablero[0][1] == tablero[0][2] != "-") or (tablero[1][0] == tablero[1][1] == tablero[1][2] != "-") or (tablero[2][0] == tablero[2][1] == tablero[2][2] != "-") or (tablero[0][0] == tablero[1][0] == tablero[2][0] != "-") or (tablero[0][1] == tablero[1][1] == tablero[2][1] != "-") or (tablero[0][2] == tablero[1][2] == tablero[2][2] != "-") or (tablero[0][0] == tablero[1][1] == tablero[2][2] != "-") or (tablero[0][2] == tablero[1][1] == tablero[2][0] != "-"):
        print("Hay un ganador, ha terminado el juego")
        break
    if contador == 9:
        print("Empate, se terminó el juego")
        break
    if contador%2 == 0:
        jugador1 = int(input("""Ingrese el movimiento del jugador 1 con un número (usa 0 para terminar el juego): 
                        |1,2,3|
                        |4,5,6|
                        |7,8,9|"""))
        match jugador1:
            case 0:
                print("Ha terminado el juego, resultado del tablero: ")
                for i in tablero:
                    print("|",end="")
                    for j in i:
                        print(j,end="|")
                    print("")
                break
            case 1:
                if tablero[0][0] == "-":
                    tablero[0][0] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 2:
                if tablero[0][1] == "-":
                    tablero[0][1] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 3:
                if tablero[0][2] == "-":
                    tablero[0][2] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 4:
                if tablero[1][0] == "-":
                    tablero[1][0] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 5:
                if tablero[1][1] == "-":
                    tablero[1][1] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 6:
                if tablero[1][2] == "-":
                    tablero[1][2] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 7:
                if tablero[2][0] == "-":
                    tablero[2][0] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 8:
                if tablero[2][1] == "-":
                    tablero[2][1] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 9:
                if tablero[2][2] == "-":
                    tablero[2][2] = "X"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
        print("Tablero: ")
        for i in tablero:
            print("|",end="")
            for j in i:
                print(j,end="|")
            print("")
        contador += 1
    else:
        jugador2 = int(input("""Ingrese el movimiento del jugador 2 con un número (usa 0 para terminar el juego): 
                        |1,2,3|
                        |4,5,6|
                        |7,8,9|"""))
        match jugador2:
            case 0:
                print("Ha terminado el juego, resultado del tablero: ")
                for i in tablero:
                    print("|",end="")
                    for j in i:
                        print(j,end="|")
                    print("")
                break
            case 1:
                if tablero[0][0] == "-":
                    tablero[0][0] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 2:
                if tablero[0][1] == "-":
                    tablero[0][1] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 3:
                if tablero[0][2] == "-":
                    tablero[0][2] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 4:
                if tablero[1][0] == "-":
                    tablero[1][0] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 5:
                if tablero[1][1] == "-":
                    tablero[1][1] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 6:
                if tablero[1][2] == "-":
                    tablero[1][2] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 7:
                if tablero[2][0] == "-":
                    tablero[2][0] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 8:
                if tablero[2][1] == "-":
                    tablero[2][1] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
            case 9:
                if tablero[2][2] == "-":
                    tablero[2][2] = "O"
                else:
                    print("Esa posición ya está ocupada...")
                    continue
        print("Tablero: ")
        for i in tablero:
            print("|",end="")
            for j in i:
                print(j,end="|")
            print("")
        contador += 1