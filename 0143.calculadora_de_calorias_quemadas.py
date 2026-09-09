def calcular_calorias(peso, minutos, intensidad):
    """Calculadora de calorias quemadas segun intensidad de entrenamiento"""
    if intensidad == "baja":
        met = 3.5
    elif intensidad == "media":
        met = 6.0
    else:
        met = 8.5

    calorias = met * 0.0175 * peso * minutos
    return calorias


print(f"\n{calcular_calorias.__doc__}")

while True:
    try:
        peso = float(input("Ingrese su peso en kg: "))
        if peso <= 0 or peso > 250:
            raise ValueError

        minutos = float(input("Ingrese los minutos de entrenamiento: "))
        if minutos <= 0 or minutos > 300:
            raise ValueError

        intensidad = input("Intensidad (baja / media / alta): ").strip().lower()
        if intensidad not in ("baja", "media", "alta"):
            raise ValueError

        break
    except ValueError:
        print("ERROR: Verifique que los numeros sean positivos y la intensidad valida.\n")

total_calorias = calcular_calorias(peso, minutos, intensidad)
print("\nResultado:")
print(f"Calorias quemadas estimadas: {total_calorias:.1f} kcal")