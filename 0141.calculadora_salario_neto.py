def calcular_salario_neto(salario_bruto, porcentaje_impuesto, retencion_seguridad):
    """Calculadora de salario neto mensual tras deducciones fiscales y previsionales"""
    monto_impuesto = salario_bruto * (porcentaje_impuesto / 100)
    monto_seguridad = salario_bruto * (retencion_seguridad / 100)
    total_descuentos = monto_impuesto + monto_seguridad
    salario_neto = salario_bruto - total_descuentos
    return salario_neto, total_descuentos


print(f"\n{calcular_salario_neto.__doc__}")

while True:
    try:
        bruto = float(input("Ingrese su salario bruto mensual ($): "))
        if bruto <= 0:
            raise ValueError

        impuesto = float(input("Ingrese el porcentaje de impuesto sobre la renta (%): "))
        if impuesto < 0 or impuesto > 60:
            raise ValueError

        seguridad = float(input("Ingrese el porcentaje de aportes previsionales/seguro (%): "))
        if seguridad < 0 or seguridad > 40:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Verifique que el salario sea positivo y los porcentajes lógicos.\n")

neto, deducciones = calcular_salario_neto(bruto, impuesto, seguridad)
print("\nDesglose de nómina:")
print(f"- Total deducciones: ${deducciones:.2f}")
print(f"- Sueldo neto a cobrar: ${neto:.2f}")