def cargar_ventas(): 
  ventas = [] 
  while True: 
    print("--- Si quiere salir del programa introduzca 'fin' ---")
    cliente = validar_texto("Ingrese el nombre del cliente: ")
    if cliente.capitalize() == "Fin": 
      break
    productos = input("Ingrese productos separados por coma: ").capitalize().split(",")
    productos = [p.strip() for p in productos]
    total = float(input("Ingrese total de la compra: "))
    venta = (cliente, productos, total)
    ventas.append(venta)
  return ventas

def procesar_ventas(ventas): 
  clientes_unicos = set()
  gastos_por_cliente = {}
  for cliente, productos, total in ventas: 
    clientes_unicos.add(cliente) 
    if cliente in gastos_por_cliente: 
      gastos_por_cliente[cliente] += total 
    else: 
      gastos_por_cliente[cliente] = total 
  return clientes_unicos, gastos_por_cliente

def mostrar_resumen(ventas, clientes_unicos, gastos): 
    print("\nClientes únicos:") 
    print(clientes_unicos) 
    print("\nGastos por cliente:") 
    for cliente, total in gastos.items(): 
      print(cliente, "->", total) 
    max_cliente = max(gastos, key=gastos.get) 
    print("\nCliente que más gastó:", max_cliente) 
    print("\nVentas mayores a 5000:")
    for venta in ventas: 
        if venta[2] > 5000:
            print(venta)

def validar_texto(mensaje):
  while True:
    texto = input(mensaje)
    if texto.isalpha():
        return texto.capitalize()
    else:
        print("Ingrese un texto válido")