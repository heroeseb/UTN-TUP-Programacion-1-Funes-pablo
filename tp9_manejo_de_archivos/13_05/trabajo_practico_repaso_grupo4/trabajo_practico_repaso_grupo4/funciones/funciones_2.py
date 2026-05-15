def validar_contrasena(contrasena):
  if len(contrasena) >= 8 and any(char.isdigit() for char in contrasena):
    return True
  else:
    return False