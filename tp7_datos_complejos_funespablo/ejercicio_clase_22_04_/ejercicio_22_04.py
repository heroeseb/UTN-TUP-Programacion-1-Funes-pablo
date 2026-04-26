# Desarrollar un programa que:
# 1. Permita cargar respuestas hasta que el usuario escriba "fin". 
# 2. Cada respuesta se guarda como una tupla:
# (nombre, edad, intereses)
# 3. Luego el programa debe: 
# • Obtener todas las edades mayores a 18
# • Generar un set de intereses únicos
# • Contar cuántas veces aparece cada interés (diccionario) 
# • Mostrar el interés más popular 
# • Mostrar las personas que tienen más de 2 intereses 
# Consigna
# Implementar funciones para:
# • cargar_encuestas()
# • procesar_encuestas(encuestas)
# • mostrar_resultados(...)

def input_string(mensaje,mensaje2):
  while True:
    input_st = input(mensaje).strip()
    if input_st.replace(' ','').isalpha():
      return input_st
    else:
      print(mensaje2)

def input_int(mensaje,mensaje2):
  while True:
    input_inter = input(mensaje).strip()
    if input_inter.isdigit() and int(input_inter) > 0:
      return int(input_inter)
    else:
      print(mensaje2)

def cargar_encuestas():
  lista = []
  while True:
    nombre = input_string('Ingrese nombre del encuestado (o "fin" para terminar): ','Ingrese un nombre correcto!')
    if nombre.lower() == "fin":
      break
    edad = input_int('Ingrese edad del encuestado: ','Ingrese una edad correcta')
    while True:
      intereses = input('Ingrese los intereses del encuestado(separando con comas): ').strip()
      if intereses.replace(',','').replace(' ','').isalpha():
        intereses_lista = [i.strip() for i in intereses.split(',')]
        break
      else:
        print('Ingrese un formato correcto!')
    tupla_encuesta = (nombre, edad, intereses_lista) 
    lista.append(tupla_encuesta) 
  return lista

encuestavalores = cargar_encuestas()

def procesar_encuestas(encuestas):
  resultado = [encuestado[1] for encuestado in encuestas if encuestado[1] > 18]
  intereses_unicos = set()
  for encuestado in encuestas:
    for interes in encuestado[2]:
      intereses_unicos.add(interes)
  intereses_diccionario = {}
  for encuestado in encuestas:
    for interes in encuestado[2]:
      if interes in intereses_diccionario:
        intereses_diccionario[interes] += 1
      else:
        intereses_diccionario[interes] = 1
  mas_popular = max(intereses_diccionario, key=intereses_diccionario.get) if intereses_diccionario else None
  personas_muchos_intereses = [e[0] for e in encuestas if len(e[2]) > 2]
  return resultado,intereses_unicos,intereses_diccionario,mas_popular,personas_muchos_intereses

mayores18,interesesunicos,interesesdiccionario,maspopular,personasconmuchosintereses = procesar_encuestas(encuestavalores)

def mostrar_resultados(edades, intereses_unicos, intereses_diccionario, mas_popular, personas_muchos_intereses):
    print("--- RESULTADOS ---")
    print("Lista de edades mayores a 18:")
    if edades:
        for edad in edades:
            print(f'- {edad}')
    else:
        print("No hay personas mayores de 18")
    print("Intereses únicos:")
    if intereses_unicos:
        for interes in intereses_unicos:
            print(f'{interes}')
    else:
        print("No hay intereses")
    print("\nCantidad de cada interés:")
    if intereses_diccionario:
        for interes, cantidad in intereses_diccionario.items():
            print(f"{interes}: {cantidad}")
    else:
        print("No hay datos")
    
    print("Interés más popular:")
    if mas_popular:
        print(mas_popular)
    else:
        print("No hay intereses cargados")
    
    print("Personas con más de 2 intereses:")
    if personas_muchos_intereses:
        for persona in personas_muchos_intereses:
            print(f'- {persona}')
    else:
        print("Nadie tiene más de 2 intereses")

mostrar_resultados(mayores18,interesesunicos,interesesdiccionario,maspopular,personasconmuchosintereses)