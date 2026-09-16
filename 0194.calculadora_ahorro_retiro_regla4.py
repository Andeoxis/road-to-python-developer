def calcular_fondo_libertad(gasto_mensual):
    """Calculadora de fondo patrimonial necesario para retiro segun la Regla del 4%"""
    gasto_anual = gasto_mensual * 12
    patrimonio_objetivo = gasto_anual * 25
    return gasto_anual, patrimonio_objetivo


print(f"\n{calcular_fondo_libertad.__doc__}")

while True:
    try:
        gasto_mes = float(input("Gasto mensual promedio deseado ($): "))
        if gasto_mes <= 0:
            raise ValueError
        break
    except ValueError:
        print("ERROR: El gasto mensual debe ser un monto positivo mayor a cero.\n")

anual, fondo = calcular_fondo_libertad(gasto_mes)
print("\nMeta financiera (Regla del 4%):")
print(f"- Gasto total anual:          ${anual:,.2f}")
print(f"- Patrimonio minimo requerido: ${fondo:,.2f}")