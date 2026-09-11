def calcular_pago_horas_extras(valor_hora_regular, horas_extras):
    """Calculadora de compensacion salarial por horas extraordinarias (recargo 50%)"""
    tarifa_extra = valor_hora_regular * 1.50
    total_extra = tarifa_extra * horas_extras
    return tarifa_extra, total_extra


print(f"\n{calcular_pago_horas_extras.__doc__}")

while True:
    try:
        tarifa = float(input("Valor de la hora ordinaria ($): "))
        if tarifa <= 0:
            raise ValueError

        horas = float(input("Cantidad de horas extras trabajadas: "))
        if horas < 0 or horas > 100:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Tarifa mayor a 0 y horas en un rango razonable.\n")

precio_hora, pago_total = calcular_pago_horas_extras(tarifa, horas)
print("\nLiquidacion de horas suplementarias:")
print(f"- Tarifa hora extra: ${precio_hora:.2f}")
print(f"- Monto total a cobrar: ${pago_total:.2f}")