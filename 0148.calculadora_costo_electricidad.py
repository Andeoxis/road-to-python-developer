def calcular_consumo_electrico(potencia_watts, horas_dia, precio_kwh):
    """Calculadora de gasto energetico mensual en base a potencia y consumo"""
    kwh_dia = (potencia_watts * horas_dia) / 1000
    kwh_mes = kwh_dia * 30
    costo_mensual = kwh_mes * precio_kwh
    return kwh_mes, costo_mensual


print(f"\n{calcular_consumo_electrico.__doc__}")

while True:
    try:
        watts = float(input("Potencia del artefacto en Watts (W): "))
        if watts <= 0 or watts > 50000:
            raise ValueError

        horas = float(input("Horas de uso promedio por dia (0.1 - 24): "))
        if horas <= 0 or horas > 24:
            raise ValueError

        tarifa = float(input("Precio por kWh ($): "))
        if tarifa <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese valores positivos y horas dentro del rango de 24h.\n")

consumo_total, gasto_total = calcular_consumo_electrico(watts, horas, tarifa)
print("\nResultado mensual (30 dias):")
print(f"- Consumo acumulado: {consumo_total:.2f} kWh")
print(f"- Costo proyectado:   ${gasto_total:.2f}")