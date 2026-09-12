def calcular_depreciacion_lineal(costo_activo, valor_residual, vida_util_anios):
    """Calculadora de depreciacion lineal anual y mensual de equipos y maquinaria"""
    depreciacion_anual = (costo_activo - valor_residual) / vida_util_anios
    depreciacion_mensual = depreciacion_anual / 12
    return depreciacion_anual, depreciacion_mensual


print(f"\n{calcular_depreciacion_lineal.__doc__}")

while True:
    try:
        costo = float(input("Valor de adquisicion del activo ($): "))
        if costo <= 0:
            raise ValueError

        residual = float(input("Valor residual o de rescate al final de la vida ($): "))
        if residual < 0 or residual >= costo:
            raise ValueError

        vida = int(input("Vida util estimada en anios: "))
        if vida <= 0 or vida > 100:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Verifique que el costo sea positivo, el valor residual menor al costo y los anios validos.\n")

anual, mensual = calcular_depreciacion_lineal(costo, residual, vida)
print("\nDesglose de depreciacion:")
print(f"- Cuota anual:   ${anual:.2f}")
print(f"- Cuota mensual: ${mensual:.2f}")