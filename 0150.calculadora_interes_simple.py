def calcular_interes_simple(capital, tasa_porcentaje, anios):
    """Calculadora financiera de interes simple y capital total acumulado"""
    interes = capital * (tasa_porcentaje / 100) * anios
    monto_total = capital + interes
    return interes, monto_total


print(f"\n{calcular_interes_simple.__doc__}")

while True:
    try:
        cap = float(input("Capital inicial ($): "))
        if cap <= 0:
            raise ValueError

        tasa = float(input("Tasa de interes anual (%): "))
        if tasa <= 0 or tasa > 100:
            raise ValueError

        tiempo = int(input("Plazo en anios: "))
        if tiempo <= 0 or tiempo > 50:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese numeros positivos y plazos razonables.\n")

ganancia, total = calcular_interes_simple(cap, tasa, tiempo)
print("\nResultado:")
print(f"- Interes generado: ${ganancia:.2f}")
print(f"- Monto final acumulado: ${total:.2f}")