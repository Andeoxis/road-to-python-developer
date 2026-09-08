def calcular_volumen_tonelaje(series, repeticiones, peso):
    """Calculadora de volumen total de entrenamiento (Tonelaje por ejercicio)"""
    reps_totales = series * repeticiones
    tonelaje_kg = reps_totales * peso
    return reps_totales, tonelaje_kg


print(f"\n{calcular_volumen_tonelaje.__doc__}")

while True:
    try:
        series = int(input("Ingrese el número de series de trabajo: "))
        if series <= 0 or series > 30:
            raise ValueError

        reps = int(input("Ingrese las repeticiones por serie: "))
        if reps <= 0 or reps > 50:
            raise ValueError

        peso = float(input("Ingrese la carga utilizada en kg: "))
        if peso <= 0 or peso > 500:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Las series, repeticiones y peso deben ser números positivos válidos.\n")

total_reps, carga_total = calcular_volumen_tonelaje(series, reps, peso)
print("\nResultado:")
print(f"- Repeticiones acumuladas: {total_reps}")
print(f"- Tonelaje total levantado: {carga_total:.1f} kg")