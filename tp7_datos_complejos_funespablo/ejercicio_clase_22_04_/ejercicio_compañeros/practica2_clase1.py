def cargar_encuestas():
  respuestas = []
  while True:
    nombre = input("Ingrese el nombre del cliente ('fin' para salir): ").strip().lower()
    if nombre != "":
      if nombre == "fin":
        return respuestas
      else:
        while True:
          edad = input("Ingrese la edad del cliente: ").strip()
          if edad.isdigit() and edad != "":
            break
          else:
            print("Error - Ingrese una edad válida")
        while True:
          intereses = input("Ingrese los interes del cliente separados por coma: ").strip().lower()
          if intereses != "":
            lista_intereses = [interes.strip() for interes in intereses.split(",")]
            break
          else:
            print("Error - Ingrese intereses válidos")
        print("Cliente cargado con éxito!")
        respuestas.append((nombre, edad, set(lista_intereses)))
    else:
      print("Error - Ingrese un nombre válido o 'fin'")

def procesar_encuesta(encuesta):
  edades_mayores = []
  intereses_unicos = set()
  cantidad_intereses = {}
  interes_popular = ""
  personas_masdos_intereses = {}
  
  lista_todos_intereses = []
  for cliente in encuesta:
    intereses = cliente[2]
    lista_intereses = list(intereses)
    for interes in lista_intereses:
      lista_todos_intereses.append(interes)
  
  for cliente in encuesta:
    nombre, edad, intereses = cliente
    if int(edad) > 18:
      edades_mayores.append(edad)
    for i in list(intereses):
      intereses_unicos.add(i)
    for j in list(intereses_unicos):
      cantidad_intereses[j] = list(lista_todos_intereses).count(j)
    interes_popular = max(cantidad_intereses, key=cantidad_intereses.get)
    if len(list(intereses)) > 2:
      personas_masdos_intereses[nombre] = len(list(intereses))
  return (edades_mayores, intereses_unicos, cantidad_intereses, interes_popular, personas_masdos_intereses)

def mostrar_resultados(resultado):
  edades_mayores, intereses_unicos, cantidad_intereses, interes_popular, personas_masdos_intereses = resultado
  print(f"""
Edades mayores a 18 años: {", ".join(edades_mayores)}
Interes únicos: {", ".join(list(intereses_unicos)).title()}
Cantidad de interés: {", ".join([f"{interes.title()} ({cantidad})" for interes, cantidad in cantidad_intereses.items()])}
Interés más popular: {interes_popular.title()}
Personas con mas de dos interéses: {", ".join([f"{persona.capitalize()} ({cantidad})" for persona, cantidad in personas_masdos_intereses.items()])}""") # Padel (2), Tenis (1)

encuesta = cargar_encuestas()
resultado = procesar_encuesta(encuesta)
mostrar_resultados(resultado)