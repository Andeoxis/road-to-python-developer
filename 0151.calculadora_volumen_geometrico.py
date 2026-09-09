def calcular_volumen_cilindro(radio, altura):
    """Calculadora de volumen y capacidad en litros de un cilindro recto"""
    pi = 3.14159265359
    volumen_m3 = pi * (radio ** 2) * altura
    litros = volumen_m3 * 1000
    return volumen_m3, litros


print(f"\n{calcular_volumen_cilindro.__doc__}")

while True:
    try:
        rad = float(input("Radio del cilindro en metros: "))
        if rad <= 0:
            raise ValueError

        alt = float(input("Altura del cilindro en metros: "))
        if alt <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Tanto el radio como la altura deben ser mayores a 0.\n")

m3, lts = calcular_volumen_cilindro(rad, alt)
print("\nResultado:")
print(f"- Capacidad en volumen: {m3:.2f} m3")
print(f"- Capacidad en liquidos: {lts:,.1f} litros")