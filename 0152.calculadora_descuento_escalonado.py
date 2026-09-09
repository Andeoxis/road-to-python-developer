def calcular_descuento_compras(monto):
    """Calculadora de descuento progresivo segun monto total de compra"""
    if monto < 100:
        descuento_pct = 0
    elif monto <= 500:
        descuento_pct = 5
    elif monto <= 1000:
        descuento_pct = 10
    else:
        descuento_pct = 15

    monto_ahorrado = monto * (descuento_pct / 100)
    total_a_pagar = monto - monto_ahorrado
    return descuento_pct, monto_ahorrado, total_a_pagar


print(f"\n{calcular_descuento_compras.__doc__}")

while True:
    try:
        subtotal = float(input("Ingrese el monto total de la compra ($): "))
        if subtotal <= 0:
            raise ValueError
        break
    except ValueError:
        print("ERROR: Ingrese un valor monetario positivo.\n")

porcentaje, ahorro, final = calcular_descuento_compras(subtotal)
print("\nResumen de facturacion:")
print(f"- Descuento aplicado: {porcentaje}%")
print(f"- Monto descontado:  ${ahorro:.2f}")
print(f"- Total a pagar:     ${final:.2f}")