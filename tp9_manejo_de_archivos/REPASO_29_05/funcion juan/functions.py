# === Funciones de validacion ===

# Funcion para validar si el usuario ingresa un entero. Parametro opcional para incluir el cero en el rango valido
def validar_entero(mensaje, incluir_cero = False):
  while True:
    try:
      valor = int(input(mensaje).strip())
      if valor < 0 or (valor == 0 and not incluir_cero):
        print("ERROR - Ingrese un numero positivo")
      else:
        return valor
    except ValueError:
      print("ERROR - Ingrese un numero valido")

# Funcion para validar si el usuario ingresa una cadena de texto
def validar_cadena(mensaje):
  while True:
    try:
      texto = input(mensaje).strip()
      if not texto:
        print("ERROR - El contenido no puede ser vacio")
      else:
        return texto
    except ValueError:
      print("ERROR - Ingrese contenido valido")

# === Funciones de muestreo ===

# Funcion para mostrar el menu completo
def mostrar_menu():
  print("=" * 32)
  print("> 1. Registro inicial de mascotas")
  print("> 2. Visualizacion de pacientes")
  print("> 3. Consulta de turnos")
  print("> 4. Reporte de mascotas sin turnos")
  print("> 5. Alta de nueva mascota")
  print("> 6. Actualizacion de turnos (asignacion / atencion)")
  print("> 7. Salir")
  print("=" * 32)
  print()

# Funcion para mostrar un paciente con toda su informacion
def mostrar_paciente(paciente):
  print(f"> {paciente["mascota"].title()} - {paciente["turnos"]} {"turno" if paciente["turnos"] == 1 else "turnos"}")

# === Funciones utiles ===

# Funcion para ver si la lista de pacientes contiene pacientes
def pacientes_listados(pacientes):
  if pacientes:
    return True
  else:
    return False

# Funcion para ver si un paciente ya existe en el sistema
def paciente_existente(pacientes, mascota):
  if any(p["mascota"].lower() == mascota.lower() for p in pacientes):
    return True
  else:
    return False

# === Funciones principales ===

# Funcion para registrar mascotas inicialmente. Pueden registrarse muchas mascotas
def registrar_mascotas(pacientes, cantidad):
  for np in range(cantidad):
    while True:
      mascota = validar_cadena(f"Ingrese el nombre del nuevo paciente{"" if cantidad == 1 else f" {np + 1}"}: ")
      if paciente_existente(pacientes, mascota):
        print("ERROR - Ya cargo esa mascota anteriormente")
      else:
        turnos = validar_entero(f"Ingrese la cantidad de turnos del nuevo paciente{"" if cantidad == 1 else f" {np + 1}"}: ", True)
        nuevo_paciente = {
          "mascota": mascota.title(),
          "turnos": turnos
        }
        pacientes.append(nuevo_paciente)
        print(f"Paciente{"" if cantidad == 1 else f" {np + 1}"} cargado correctamente")
        break
  print()
  return pacientes

# Funcion para visualizar a todos los pacientes del sistema
def visualizar_pacientes(pacientes):
  if pacientes_listados(pacientes):
    print("Pacientes cargados en el sistema:")
    for p in pacientes:
      mostrar_paciente(p)
    print()
  else:
    print("ERROR - No hay pacientes cargados en el sistema")
    print()

# Funcion para consultar la cantidad de turnos de un paciente
def consulta_turnos(pacientes):
  if pacientes_listados(pacientes):
    mascota = validar_cadena("Ingrese el nombre del paciente: ")
    if paciente_existente(pacientes, mascota):
      paciente = next(p for p in pacientes if p["mascota"].lower() == mascota.lower())
      mostrar_paciente(paciente)
    else:
      print("ERROR - No se encontro un paciente con ese nombre")
  else:
    print("ERROR - No hay pacientes cargados en el sistema")
    print()

# Funcion para mostrar las mascotas sin turnos
def reporte_mascotas_sin_turnos(pacientes):
  if pacientes_listados(pacientes):
    if any(p["turnos"] == 0 for p in pacientes):
      print("Pacientes sin turnos cargados en el sistema")
      for p in pacientes:
        if p["turnos"] == 0:
          mostrar_paciente(p)
      print()
    else:
      print("ERROR - No se encontraron pacientes sin turnos")
      print()
  else:
    print("ERROR - No hay pacientes cargados en el sistema")
    print()

# Funcion para cargar un nuevo paciente en el sistema
def alta_nuevo_paciente(pacientes):
  mascota = validar_cadena("Ingrese el nombre del nuevo paciente: ")
  if paciente_existente(pacientes, mascota):
    print("ERROR - Ya hay un paciente con ese nombre")
    print()
    return pacientes
  else:
    turnos = validar_entero("Ingrese la cantidad de turnos del nuevo paciente: ", True)
    nuevo_paciente = {
      "mascota": mascota.title(),
      "turnos": turnos
    }
    pacientes.append(nuevo_paciente)
    print("Paciente cargado correctamente")
    print()
    return pacientes

# Funcion para registrar atencion o asignacion de turnos a un paciente
def actualizar_turno(pacientes):
  if pacientes_listados(pacientes):
    mascota = validar_cadena("Ingrese el nombre del paciente: ")
    if paciente_existente(pacientes, mascota):
      while True:
        opcion = validar_entero("Ingrese 1 para marcar atencion del paciente o 2 para asignar un turno al paciente: ")
        match opcion:
          case 1:
            for p in pacientes:
              if p["mascota"].lower() == mascota.lower():
                if p["turnos"] < 1:
                  print("ERROR - No puede dar atencion al paciente porque no tiene turnos")
                  print()
                  return pacientes
                else:
                  p["turnos"] -= 1
                  print("Paciente atendido correctamente")
                  print()
                  return pacientes
          case 2:
            for p in pacientes:
              if p["mascota"].lower() == mascota.lower():
                  p["turnos"] += 1
                  print("Paciente asignado correctamente")
                  print()
                  return pacientes
          case _:
            print("ERROR - Ingrese una opcion valida")
    else:
      print("ERROR - No se encontro un paciente con ese nombre")
      print()
      return pacientes
  else:
    print("ERROR - No hay pacientes cargados en el sistema")
    print()
    return pacientes