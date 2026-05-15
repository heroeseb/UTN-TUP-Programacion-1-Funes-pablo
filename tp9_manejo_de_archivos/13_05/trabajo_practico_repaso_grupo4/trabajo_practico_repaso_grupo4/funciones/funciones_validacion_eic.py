def validacion_entero(mensaje1, mensaje2 = None, negativo = True):
  while True:
    try: 
      numero = int(input(mensaje1))
      if negativo:
        if numero < 0:
          print("ERROR! No se permiten numero negativos")
          continue
      if mensaje2 != None:
        print(mensaje2) 
      return int(numero)
    except ValueError: 
      print("ERROR! Debe ingresar un numero entero")
    except Exception as e: 
      print(f"Ha ocurrido un error inesperado: {e}")

def validacion_float(mensaje1, mensaje2 = None, negativo = True):
  while True:
    try:
      numero = float(input(mensaje1))
      if negativo:
        if numero <= 0:
          print("ERROR! No se permiten numero negativos o cero")
          continue
      if mensaje2 != None:
        print(mensaje2)
      return float(numero)
    except ValueError:
      print("ERROR! Debe ingresar un numero positivo")
    except Exception as e:
      print(f"Ha ocurrido un error inesperado: {e}")

def validacion_texto(mensaje1, mensaje2 = None):
  while True:
    try:
      texto = input(mensaje1).strip()
      if not texto:
        print("ERROR! No se permiten campos vacios")
        continue
      if mensaje2 != None:
        print(mensaje2)
      return texto
    except ValueError:
      print("ERROR! Debe ingresar un texto válido")
    except Exception as e:
      print(f"Ha ocurrido un error inesperado: {e}")