def calcular_nota_final(teoria, practica, asistencia):
    """Calculadora de promedio ponderado y calificacion academica"""
    promedio = (teoria * 0.40) + (practica * 0.40) + (asistencia * 0.20)
    estado = "Aprobado" if promedio >= 51.0 else "Reprobado"
    return promedio, estado


print(f"\n{calcular_nota_final.__doc__}")

while True:
    try:
        teoria = float(input("Nota de teoria (0-100): "))
        if teoria < 0 or teoria > 100:
            raise ValueError

        practica = float(input("Nota de practica (0-100): "))
        if practica < 0 or practica > 100:
            raise ValueError

        asistencia = float(input("Nota de asistencia (0-100): "))
        if asistencia < 0 or asistencia > 100:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Las tres notas deben estar comprendidas entre 0 y 100.\n")

nota, estado = calcular_nota_final(teoria, practica, asistencia)
print("\nResultado Academico:")
print(f"Nota final ponderada: {nota:.1f} pts - Estado: {estado}")