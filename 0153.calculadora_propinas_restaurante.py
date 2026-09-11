def calcular_propina_servicio(total_consumo, nivel_servicio):
    """Calculadora de propina segun la percepcion del servicio recibido"""
    porcentajes = {
        "malo": 5,
        "bueno": 10,
        "excelente": 15
    }
    pct = porcentajes[nivel_servicio]
    propina = total_consumo * (pct / 100)
    total_pagar = total_consumo + propina
    return pct, propina, total_pagar


print(f"\n{calcular_propina_servicio.__doc__}")

while True:
    try:
        consumo = float(input("Ingrese el total consumido ($): "))
        if consumo <= 0:
            raise ValueError

        servicio = input("Calidad del servicio (malo / bueno / excelente): ").strip().lower()
        if servicio not in ("malo", "bueno", "excelente"):
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese un monto positivo y una calificacion valida.\n")

pct, prop, gran_total = calcular_propina_servicio(consumo, servicio)
print("\nResumen de pago:")
print(f"- Porcentaje asignado: {pct}%")
print(f"- Monto de propina:    ${prop:.2f}")
print(f"- Total final:         ${gran_total:.2f}")