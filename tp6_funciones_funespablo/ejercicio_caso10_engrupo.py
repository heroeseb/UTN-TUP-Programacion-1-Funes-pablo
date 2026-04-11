habitaciones = []
estados = []

while True:
  print(''' ---- Menú de gestión del Hotel ---- 
1- Ingreso de Habitaciones (Número de habitación)
2- Ingreso Estado de habitaciones (Libre/Ocupada)
3- Estado General (Habitación "x" - Estado "x")
4- Estado de Habitación (Habitación específica)
5- Lista de Estado (Habitaciones específicas)
6- Añadir una habitación (Habitación y su estado)
7- Cambio de Estado (Habitación específica)
8- Salir del menú''')
  opcion = input("Seleccione una opción: ")
  match opcion:
      case "1":
          while True:
              cantidad = input("¿Cuantas habitaciones desea ingresar?: ").strip()
              if not cantidad.isdigit():
                  print("Error, por favor ingrese un número válido. ")
              else:
                  cantidad = int(cantidad)
                  break
          for habitacion in range(cantidad):
              while True:
                  numero = input("Por favor, ingrese el número de habitación: ").strip()
                  if not numero.isdigit():
                      print("Error, por favor solo ingrese solo números. ")
                  else:
                      numero = int(numero)
                      if numero in habitaciones:
                          print("Error, la habitación ingresada ya existe. ")
                      else:
                          habitaciones.append(numero)
                          estados.append("0")
                          print("Habitación agregada correctamente. ")
                          break                
      case "2":
            while True:
                for habitacion in habitaciones:
                  while True:
                    estado_nuevo = input(f"Ingrese el estado de habitación {habitacion} ({"Ocupada" if estados[habitaciones.index(habitacion)] == "1" else "Libre"}) (Ingrese 1 para ocupada y 0 para libre): ")
                    if estado_nuevo in ["0", "1"]:
                      estados[habitaciones.index(habitacion)] = estado_nuevo
                      print(f"Perfecto!! La habitación {habitacion} está {"Ocupada" if estado_nuevo == "1" else "Libre"}!!")
                      break
                    else:
                      print("ERROR")
                break
      case "3":
          if len(habitaciones) == 0:
            print("No hay habitaciones disponibles.")
          else:
            print("\nEstados de las habitaciones: ")
            for i in range(len(habitaciones)):
                if estados[i] == "0":
                  estado = "Libre"
                else:
                  estado = "Ocupada"
                print(f"Habitación {habitaciones[i]}: {estado}")
      case "4":
        while True:
          verificar=input("Ingrese el número de la habitación: ").strip()
          if verificar not in habitaciones:
            print("Error. No existe esa habitacion")
          else:
            indice_verificacion=habitaciones.index(verificar)
            if estados[indice_verificacion]=="0":
              estado="libre"
            else:
              estado="ocupada"
            print(f"El estado de la habitación {verificar} es: {estado}")
            break
      case "5":
          while True:
            print("""
        1) Ver habitaciones ocupadas
        2) Ver habitaciones libres
        3) Salir
        """)
            EleccionHabitacion = input("¿Que desea hacer?: ")
            if EleccionHabitacion.isdigit and not "" or " ":
              match int(EleccionHabitacion):
                case 1:
                  if 1 in estados:
                    for i in range(len(estados)):
                      if estados[i] == "1":
                        print(f"{habitaciones[i]}")
                case 2:
                  if 0 in estados:
                    for i in range(len(estados)):
                      if estados[i] == "0":
                        print(f"{habitaciones[i]}")
                case 3:
                  break
                case _:
                  print("Ingrese un valor valido.")
            else:
                print("Por favor, ingrese un valor valido.")
      case "6":#Pablito
          nueva = int(input("Ingrese el numero de la nueva habitación: "))
          if nueva in habitaciones:
            print("La habitación ya existe ")
          elif nueva < 1:
            print("numero invalido")
          else:
            habitaciones.append(nueva)
            estado.append(0)
            print("Habitacion agregada correctamente")
      case "7": # Arango
          print("> Cambio de estado de habitación")
          while True:
              habitacion = input("Ingrese el número de la habitación para cambiar el estado: ").strip()
              if habitacion.isdigit() and habitacion != "":
                  if habitacion in habitaciones:
                    print(f"Habitación {habitacion} - Estado actual: {"Ocupada" if estados[habitaciones.index(habitacion)] == "1" else "Libre"}")
                    input("Presione ENTER para cambiar el estado actual... ")
                    if estados[habitaciones.index(habitacion)] == "1":
                        estados[habitaciones.index(habitacion)] = "0"
                    else:
                        estados[habitaciones.index(habitacion)] = "1"
                  else:
                    print("ERROR - Esa habitación no está en el sistema")
              else:
                print("ERROR - Ingrese un número")
      case "8":
          print("Gracias por usar el sistema - Vuelva pronto!")
          break
      case _:
          print("Opción no válida. Reintentelo")