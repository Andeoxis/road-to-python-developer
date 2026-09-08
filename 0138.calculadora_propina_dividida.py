def calcular_cuenta_dividida(total_cuenta, porcentaje_propina, personas):
    """Calculadora de propina y división equitativa de cuenta por persona"""
    propina_total = total_cuenta * (porcentaje_propina / 100)
    gran_total = total_cuenta + propina_total
    pago_por_persona = gran_total / personas
    return propina_total, gran_total, pago_por_persona


print(f"\n{calcular_cuenta_dividida.__doc__}")

while True:
    try:
        cuenta = float(input("Ingrese el total de la cuenta ($): "))
        if cuenta <= 0:
            raise ValueError

        propina = float(input("Ingrese el porcentaje de propina (ej: 10, 15): "))
        if propina < 0 or propina > 100:
            raise ValueError

        comensales = int(input("Ingrese el número de personas a dividir: "))
        if comensales <= 0 or comensales > 50:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese valores válidos (montos positivos y personas > 0).\n")

propina_total, total_final, por_cabeza = calcular_cuenta_dividida(cuenta, propina, comensales)
print("\nResultado:")
print(f"- Propina acumulada:  ${propina_total:.2f}")
print(f"- Cuenta total:       ${total_final:.2f}")
print(f"- Cada persona paga:  ${por_cabeza:.2f}")