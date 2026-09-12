def estimar_gasto_caminata(pasos, peso_kg):
    """Calculadora de distancia recorrida aproximada y gasto calorico por pasos"""
    distancia_km = (pasos * 0.75) / 1000
    calorias_quemadas = distancia_km * peso_kg * 0.75
    return distancia_km, calorias_quemadas


print(f"\n{estimar_gasto_caminata.__doc__}")

while True:
    try:
        cant_pasos = int(input("Numero de pasos caminados: "))
        if cant_pasos <= 0 or cant_pasos > 150000:
            raise ValueError

        peso = float(input("Peso corporal en kg: "))
        if peso <= 30 or peso > 250:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese valores coherentes (pasos > 0 y peso entre 30 y 250 kg).\n")

distancia, kcal = estimar_gasto_caminata(cant_pasos, peso)
print("\nMetricas de la caminata:")
print(f"- Distancia estimada:  {distancia:.2f} km")
print(f"- Energia consumida:   {kcal:.1f} kcal")