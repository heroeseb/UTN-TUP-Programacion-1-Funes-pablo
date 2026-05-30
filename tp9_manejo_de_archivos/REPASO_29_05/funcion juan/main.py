from functions import *

pacientes = [
  {
    "mascota": "Tobi",
    "turnos": 6
  },
  {
    "mascota": "Pedro",
    "turnos": 12
  },
  {
    "mascota": "Coco",
    "turnos": 0
  }
]

while True:
  mostrar_menu()
  opcion = validar_entero("Seleccione una opcion: ")
  
  match opcion:
    case 1:
      if pacientes_listados(pacientes):
        print("ERROR - No puede volver a hacer una carga inicial de mascotas. Use la opcion 5 para dar de alta una nueva mascota")
        print()
      else:
        cantidad = validar_entero("Ingrese la cantidad de mascotas que desea registrar: ")
        pacientes = registrar_mascotas(pacientes, cantidad)
    case 2:
      visualizar_pacientes(pacientes)
    case 3:
      consulta_turnos(pacientes)
    case 4:
      reporte_mascotas_sin_turnos(pacientes)
    case 5:
      pacientes = alta_nuevo_paciente(pacientes)
    case 6:
      pacientes = actualizar_turno(pacientes)
    case 7:
      print("SALIR - Gracias por usar el sistema")
      break
    case _:
      print("ERROR - Ingrese una opcion valida")