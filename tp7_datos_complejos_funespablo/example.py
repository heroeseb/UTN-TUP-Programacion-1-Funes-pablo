inventario = [
    {"Pais": "Argentina",
    "Capital": "Buenos Aires",
    "Poblacion": 46000000,
    "Superficie": 12000},
    
    {"Pais": "Francia",
    "Capital": "Paris",
    "Poblacion": 3000000,
    "Superficie": 120}
]

for i in range(len(inventario)):
    for key in inventario[i].keys():
        print(inventario[i][key])

for i in range(len(inventario)):
    print(f"Pais N° {i+1} de la lista: ")
    for key in inventario[i].keys():
        print(f"{key} : {inventario[i][key]}")
    print("=" * 30)

for i in range(len(inventario)):
    print(f"Pais N° {i+1} de la lista: ")
    for key in inventario[i].keys():
        if inventario[i][key] == "Argentina":
            inventario[i]["Poblacion"] = 500000

bandera = False

for i in range(len(inventario)):
    for key in inventario[i].keys():
        if inventario[i][key] == "Argentina":
            inventario[i]["Poblacion"] = 500000
            bandera = True
            break
    if bandera:
        break

def mostrar_inventario(lista):
    for herramienta in lista:
        print(f"{herramienta['herramienta']} : $ {herramienta['cantidad']}")

if __name__ == "__main__":
    lista = [
        {"herramienta": "Destornillador", "cantidad": 3},
        {"herramienta": "Cinta metrica", "cantidad": 4}
    ]

    mostrar_inventario(lista)

def validar_duplicado(nombre_buscado, lista):
    for herramienta in lista:
        if herramienta["herramienta"] == nombre_buscado:
            print(f"La herramienta {nombre_buscado} ya existe")
            return True
    return False

# match opcion:
#     case "1":
#         cantidad = cantidad_a_ingresar()
#         for i in range(cantidad):
#             herramienta = solicita_nombre_herramienta()
#             while validar_duplicado(herramienta, inventario):
#                 herramienta = solicita_nombre_herramienta()
            
#             inventario.append({
#                 "herramienta": herramienta,
#                 "cantidad": 0
#             })
        
#         print(cantidad)
#     case "2":
#         # Continúa el código...