def calcular_costo_arriendo(dias_alquiler, precio_por_dia, seguro_opcional):
    """Calculadora de costo de arriendo con tarifa base y seguro diario"""
    costo_base = dias_alquiler * precio_por_dia
    costo_seguro = (dias_alquiler * 15.0) if seguro_opcional == "s" else 0.0
    total = costo_base + costo_seguro
    return costo_base, costo_seguro, total


print(f"\n{calcular_costo_arriendo.__doc__}")

while True:
    try:
        dias = int(input("Dias de alquiler requeridos: "))
        if dias <= 0 or dias > 365:
            raise ValueError

        tarifa = float(input("Tarifa base por dia ($): "))
        if tarifa <= 0:
            raise ValueError

        seguro = input("Desea incluir seguro ($15/dia)? (s/n): ").strip().lower()
        if seguro not in ("s", "n"):
            raise ValueError

        break
    except ValueError:
        print("ERROR: Verifique los dias (> 0), precio diario y respuesta de seguro (s/n).\n")

base, seg, gran_total = calcular_costo_arriendo(dias, tarifa, seguro)
print("\nResumen de arriendo:")
print(f"- Costo base:   ${base:.2f}")
print(f"- Costo seguro: ${seg:.2f}")
print(f"- Total a pagar: ${gran_total:.2f}")