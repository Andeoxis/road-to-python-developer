def calcular_volumen_cono(radio, altura):
    """Calculadora de volumen geometrico de un cono circular recto"""
    pi = 3.141592653589793
    volumen = (pi * (radio ** 2) * altura) / 3
    return volumen


print(f"\n{calcular_volumen_cono.__doc__}")

while True:
    try:
        rad = float(input("Radio de la base en metros: "))
        if rad <= 0:
            raise ValueError

        alt = float(input("Altura del cono en metros: "))
        if alt <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Tanto el radio como la altura deben ser mayores a cero.\n")

vol = calcular_volumen_cono(rad, alt)
print("\nResultado:")
print(f"Volumen del cono: {vol:.2f} m3")