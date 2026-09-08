def calcular_circuito_electrico(voltaje, corriente):
    """Calculadora de potencia activa (Watts) y resistencia equivalente (Ohms) (Ley de Ohm/Joule)"""
    potencia = voltaje * corriente
    resistencia = voltaje / corriente
    return potencia, resistencia


print(f"\n{calcular_circuito_electrico.__doc__}")

while True:
    try:
        volt = float(input("Ingrese la tensión eléctrica en Voltios (V): "))
        if volt <= 0 or volt > 1000:
            raise ValueError

        amper = float(input("Ingrese la intensidad de corriente en Amperios (A): "))
        if amper <= 0 or amper > 500:
            raise ValueError

        break
    except ValueError:
        print("ERROR: La tensión y corriente deben ser valores positivos mayores a cero.\n")

watts, ohms = calcular_circuito_electrico(volt, amper)
print("\nValores calculados:")
print(f"- Potencia disipada: {watts:.2f} W")
print(f"- Resistencia estimada: {ohms:.2f} Ω")