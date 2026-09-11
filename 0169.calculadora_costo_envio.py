def calcular_tarifa_envio(peso_kg, tipo_entrega):
    """Calculadora de costo logistico segun peso y prioridad de envio"""
    costo_base = peso_kg * 4.50
    adicional = 15.0 if tipo_entrega == "express" else 0.0
    total = costo_base + adicional
    return costo_base, adicional, total


print(f"\n{calcular_tarifa_envio.__doc__}")

while True:
    try:
        peso = float(input("Peso del paquete en kg: "))
        if peso <= 0 or peso > 100:
            raise ValueError

        tipo = input("Tipo de envio (estandar / express): ").strip().lower()
        if tipo not in ("estandar", "express"):
            raise ValueError

        break
    except ValueError:
        print("ERROR: Peso fuera de rango o modalidad no reconocida.\n")

base, recargo, monto_final = calcular_tarifa_envio(peso, tipo)
print("\nDetalle del envio:")
print(f"- Costo por peso:     ${base:.2f}")
print(f"- Recargo modalidad:  ${recargo:.2f}")
print(f"- Costo total:        ${monto_final:.2f}")