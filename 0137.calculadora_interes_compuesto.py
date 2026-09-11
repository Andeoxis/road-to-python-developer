def calcular_interes_compuesto(capital, tasa_anual, meses):
    """Calculadora de crecimiento financiero con interés compuesto mensual"""
    tasa_mensual = (tasa_anual / 100) / 12
    capital_final = capital * ((1 + tasa_mensual) ** meses)
    ganancia = capital_final - capital
    return capital_final, ganancia


print(f"\n{calcular_interes_compuesto.__doc__}")

while True:
    try:
        capital = float(input("Ingrese el monto inicial a invertir ($): "))
        if capital <= 0:
            raise ValueError

        tasa = float(input("Ingrese el porcentaje de tasa de interés anual (%): "))
        if tasa <= 0 or tasa > 100:
            raise ValueError

        meses = int(input("Ingrese el plazo de inversión en meses: "))
        if meses <= 0 or meses > 600:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Todos los valores deben ser positivos y estar dentro de rangos lógicos.\n")

monto_final, rendimiento = calcular_interes_compuesto(capital, tasa, meses)
print("\nResultado:")
print(f"- Capital final proyectado: ${monto_final:.2f}")
print(f"- Interés ganado:           ${rendimiento:.2f}")