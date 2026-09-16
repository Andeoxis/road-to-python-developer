def calcular_ley_hooke(constante_k, deformacion_x):
    """Calculadora de fuerza restauradora elastica mediante la Ley de Hooke (F = k * x)"""
    fuerza = constante_k * deformacion_x
    return fuerza


print(f"\n{calcular_ley_hooke.__doc__}")

while True:
    try:
        k = float(input("Constante elastica del resorte en N/m: "))
        if k <= 0 or k > 50000:
            raise ValueError

        x = float(input("Elongacion o compresion en metros (m): "))
        if x <= 0 or x > 50:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Tanto la constante (k) como la deformacion (x) deben ser mayores a 0.\n")

fuerza_n = calcular_ley_hooke(k, x)
print("\nResultado:")
print(f"Fuerza elastica generada: {fuerza_n:.2f} N")