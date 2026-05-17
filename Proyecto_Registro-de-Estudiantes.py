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
    
    # Determinar el estado del estudiante
    estado_academico = ""
    if total_faltas >= 0.3 * clases:
        estado_academico = "Reprobado por faltas (incluyendo tardanzas)"
        print(f"\nEl estudiante está {estado_academico}.\n")
    elif promedio_final < 12.5:
        estado_academico = "Reprobado por nota"
        print(f"\nEl estudiante está {estado_academico}.\n")
    else:
        estado_academico = "Aprobado"
        print(f"\nEl estudiante está {estado_academico}.\n")

    # Agregar al arreglo principal
    estudiantes.append({
        "nombre": nombre,
        "notas": [pc01, pc02, ep, ef],
        "promedio_final": promedio_final,
        "clases": clases,
        "faltas": faltas,
        "tardanzas": tardanzas,
        "estado": estado_academico,
    })

    print(f"Estudiante {nombre} registrado correctamente.\n")
    
    # Estructura repetitiva + cadenas
# ------------------------------

def buscar_estudiante():
    print("\n--- Buscar estudiante ---")

    while True:
        nombre_buscar = input("Ingrese nombre a buscar: ").strip().lower()
        if nombre_buscar.replace(' ', '').isalpha():
            break
        else:
            print("Nombre de búsqueda inválido. Solo se admiten caracteres de texto. Intente de nuevo.")
    # Cadenas
    for est in estudiantes:
        if est["nombre"].lower() == nombre_buscar:
            print(f"\nEstudiante: {est['nombre']}")
            print(f"Notas: {est['notas']}")
            print(f"Promedio final: {est['promedio_final']:.2f}\n")
            print(f"Clases: {est['clases']}")
            print(f"Faltas: {est['faltas']}")
            print(f"Tardanzas: {est['tardanzas']}")
            print(f"\nEstado Académico: {est['estado']}.\n")
            return

    print("No se encontró el estudiante.\n"
    
def mostrar_reporte():
    print("\n--- Reporte general ---")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.\n")
        return

    # Estructura repetitiva
    for est in estudiantes:
        print(f"Estudiante: {est['nombre']} - Promedio final: {est['promedio_final']:.2f} - Faltas: {est['faltas']} - Tardanzas: {est['tardanzas']} - Estado Académico: {est['estado']}")

    print()
    
# ------------------------------
# Menú principal (estructura repetitiva + selectiva)
# ------------------------------

while True:
    print("===== Sistema de Gestión =====")
    print("1. Registrar estudiante")
    print("2. Buscar estudiante")
    print("3. Mostrar reporte")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # Estructura selectiva
    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        buscar_estudiante()
    elif opcion == "3":
        mostrar_reporte()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida. Intente nuevamente.\n")