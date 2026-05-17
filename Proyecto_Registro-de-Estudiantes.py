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