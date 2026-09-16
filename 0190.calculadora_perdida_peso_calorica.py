def calcular_deficit_grasa(deficit_diario_kcal, dias):
    """Calculadora de perdida teorica de tejido adiposo segun deficit calorico acumulado"""
    deficit_acumulado = deficit_diario_kcal * dias
    grasa_perdida_kg = deficit_acumulado / 7700
    return deficit_acumulado, grasa_perdida_kg


print(f"\n{calcular_deficit_grasa.__doc__}")

while True:
    try:
        deficit = float(input("Deficit calorico diario en kcal (ej: 300 - 1000): "))
        if deficit <= 0 or deficit > 2000:
            raise ValueError

        tiempo_dias = int(input("Cantidad de dias proyectados: "))
        if tiempo_dias <= 0 or tiempo_dias > 365:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Deficit diario debe ser entre 1 y 2000 kcal, y dias entre 1 y 365.\n")

acumulado, kg_grasa = calcular_deficit_grasa(deficit, tiempo_dias)
print("\nProyeccion de perdida:")
print(f"- Deficit total acumulado: {acumulado:.0f} kcal")
print(f"- Grasa estimada a perder: {kg_grasa:.2f} kg")