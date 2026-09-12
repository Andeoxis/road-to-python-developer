def convertir_presion_psi(psi):
    """Conversor de presion desde PSI a Bares y KiloPascales (kPa)"""
    bar = psi * 0.0689476
    kpa = psi * 6.89476
    return bar, kpa


print(f"\n{convertir_presion_psi.__doc__}")

while True:
    try:
        presion_psi = float(input("Ingrese la presion en PSI: "))
        if presion_psi < 0 or presion_psi > 10000:
            raise ValueError
        break
    except ValueError:
        print("ERROR: Ingrese un valor de presion positivo dentro de rangos normales.\n")

bares, kilopascales = convertir_presion_psi(presion_psi)
print("\nEquivalencias:")
print(f"- Presion en Bares:       {bares:.3f} bar")
print(f"- Presion en KiloPascales: {kilopascales:.2f} kPa")