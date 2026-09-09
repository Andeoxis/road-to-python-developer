def calcular_1rm(peso, repeticiones):
    """Calculadora de 1RM teorico mediante la formula de Epley"""
    if repeticiones == 1:
        return peso
    return peso * (1 + (repeticiones / 30))


print(f"\n{calcular_1rm.__doc__}")

while True:
    try:
        peso = float(input("Ingrese la carga levantada en kg: "))
        if peso <= 0 or peso > 500:
            raise ValueError

        reps = int(input("Ingrese las repeticiones completadas (1-12): "))
        if reps < 1 or reps > 12:
            raise ValueError

        break
    except ValueError:
        print("ERROR: El peso debe ser mayor a 0 y las repeticiones entre 1 y 12.\n")

rm_estimado = calcular_1rm(peso, reps)
print("\nResultado:")
print(f"Tu repeticion maxima (1RM) estimada es: {rm_estimado:.1f} kg")