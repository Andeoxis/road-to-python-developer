def calcular_depreciacion_anual(valor_inicial, tasa_anual, anios):
    """Calculadora de depreciacion de activos segun tasa anual compuesta"""
    valor_actual = valor_inicial * ((1 - (tasa_anual / 100)) ** anios)
    perdida = valor_inicial - valor_actual
    return valor_actual, perdida


print(f"\n{calcular_depreciacion_anual.__doc__}")

while True:
    try:
        precio_orig = float(input("Precio inicial del vehiculo ($): "))
        if precio_orig <= 0:
            raise ValueError

        depreciacion = float(input("Tasa de depreciacion anual (%): "))
        if depreciacion <= 0 or depreciacion >= 100:
            raise ValueError

        antiguedad = int(input("Antiguedad en anios: "))
        if antiguedad < 0 or antiguedad > 50:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese valores coherentes (precios > 0, tasa entre 0 y 100).\n")

valor_residual, perdida_total = calcular_depreciacion_anual(precio_orig, depreciacion, antiguedad)
print("\nResultado financiero:")
print(f"- Valor estimado actual: ${valor_residual:.2f}")
print(f"- Valor depreciado:      ${perdida_total:.2f}")