def calcular_distancia_frenado(velocidad_kmh, estado_suelo):
    """Calculadora de distancia de frenado segun velocidad y condiciones del asfalto"""
    coeficiente = 0.7 if estado_suelo == "seco" else 0.4
    velocidad_ms = velocidad_kmh / 3.6
    distancia = (velocidad_ms ** 2) / (2 * 9.8 * coeficiente)
    return distancia


print(f"\n{calcular_distancia_frenado.__doc__}")

while True:
    try:
        vel = float(input("Ingrese la velocidad en km/h: "))
        if vel <= 0 or vel > 350:
            raise ValueError

        suelo = input("Estado de la calzada (seco / mojado): ").strip().lower()
        if suelo not in ("seco", "mojado"):
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese una velocidad valida y 'seco' o 'mojado' para el suelo.\n")

metros = calcular_distancia_frenado(vel, suelo)
print("\nResultado:")
print(f"Distancia minima de detencion: {metros:.2f} metros")