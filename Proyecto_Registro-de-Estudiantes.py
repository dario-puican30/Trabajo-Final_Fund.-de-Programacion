# ------------------------------
# Sistema de Gestión de Estudiantes
# ------------------------------


# Registro de datos, validaciones, cálculos y almacenamiento
# ------------------------------
estudiantes = []   # Arreglo principal

def registrar_estudiante():
    print("\n--- Registrar estudiante ---")

    while True:
        nombre = input("Nombre del estudiante: ").strip()
        if nombre.replace(' ', '').isalpha():
            break
        else:
            print("Nombre inválido. Solo se admiten caracteres de texto. Intente de nuevo.")
            
    # Registrar notas pc01, pc02, ep y ef
    while True:
      pc01 = float(input("Ingrese la nota de PC01: "))
      if pc01 <= 20:
        break
      else:
        print("La nota de PC01 no puede ser mayor a 20. Intente de nuevo.")
    while True:
      pc02 = float(input("Ingrese la nota de PC02: "))
      if pc02 <= 20:
        break
      else:
        print("La nota de PC02 no puede ser mayor a 20. Intente de nuevo.")
    while True:
      ep = float(input("Ingrese la nota de EP: "))
      if ep <= 20:
        break
      else:
        print("La nota de EP no puede ser mayor a 20. Intente de nuevo.")
    while True:
      ef = float(input("Ingrese la nota de EF: "))
      if ef <= 20:
        break
      else:
        print("La nota de EF no puede ser mayor a 20. Intente de nuevo.")
        
    # Fórmula: Promedio Final = PC01 * 0.2 + PC02 * 0.2 + EP * 0.2 + EF * 0.4
    promedio_final = pc01 * 0.2 + pc02 * 0.2 + ep * 0.2 + ef * 0.4
    print(f"La nota final es: {promedio_final:.2f}.\n")
    
    # Registrar faltas y tardanzas
    while True:
      clases = int(input("Ingrese el número total de clases: "))
      if clases > 0:
        break
      else:
        print("El número de clases debe ser mayor que cero. Intente de nuevo.")
    while True:
      faltas = int(input("Ingrese el número total de faltas: "))
      if faltas <= clases:
        break
      else:
        print("El número de faltas no puede ser mayor que el número de clases. Intente de nuevo.")
    while True:
      tardanzas = int(input("Ingrese el número total de tardanzas: "))
      if tardanzas <= clases:
        break
      else:
        print("El número de tardanzas no puedes ser mayor al número de clases. Intente de nuevo.")

    # Calcular faltas equivalentes por tardanzas
    faltas_por_tardanzas = tardanzas // 2
    total_faltas = faltas + faltas_por_tardanzas