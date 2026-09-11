def calcular_factura_iva(precio_base, porcentaje_iva):
    """Calculadora de impuesto al valor agregado y precio final de venta"""
    iva_monto = precio_base * (porcentaje_iva / 100)
    precio_total = precio_base + iva_monto
    return iva_monto, precio_total


print(f"\n{calcular_factura_iva.__doc__}")

while True:
    try:
        base = float(input("Precio base sin impuestos ($): "))
        if base <= 0:
            raise ValueError

        iva = float(input("Porcentaje de IVA aplicable (%): "))
        if iva < 0 or iva > 50:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese un precio base positivo y un IVA coherente.\n")

monto_impuesto, total = calcular_factura_iva(base, iva)
print("\nDesglose de factura:")
print(f"- Monto por IVA: ${monto_impuesto:.2f}")
print(f"- Total a pagar: ${total:.2f}")