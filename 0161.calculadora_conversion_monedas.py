def convertir_divisa(monto_origen, tipo_cambio):
    """Calculadora de conversion de divisas segun tipo de cambio personalizado"""
    monto_convertido = monto_origen * tipo_cambio
    return monto_convertido


print(f"\n{convertir_divisa.__doc__}")

while True:
    try:
        monto = float(input("Monto en moneda local: "))
        if monto <= 0:
            raise ValueError

        tasa = float(input("Tipo de cambio respecto a la divisa destino: "))
        if tasa <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Tanto el monto como la tasa de cambio deben ser positivos.\n")

conversion = convertir_divisa(monto, tasa)
print("\nResultado cambiario:")
print(f"Monto final equivalente: {conversion:.2f}")