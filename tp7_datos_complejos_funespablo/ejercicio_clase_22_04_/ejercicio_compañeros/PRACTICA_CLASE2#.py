from FUNCIONES_CLASE import *

print("Bienvenido al Almacen Sr. Batata")
ventas=cargar_ventas() 
if len(ventas) > 0:  
    clientes, gastos = procesar_ventas(ventas)
    mostrar_resumen(ventas, clientes, gastos)
else: 
    print("No se ingresaron ventas") 
