def calcular_geometria_rectangulo(base, altura):
    """Calculadora de area de superficie y perimetro de un rectangulo"""
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro


print(f"\n{calcular_geometria_rectangulo.__doc__}")

while True:
    try:
        b = float(input("Ingrese la base en metros: "))
        h = float(input("Ingrese la altura en metros: "))
        if b <= 0 or h <= 0:
            raise ValueError
        break
    except ValueError:
        print("ERROR: Tanto la base como la altura deben ser mayores a 0.\n")

ar, per = calcular_geometria_rectangulo(b, h)
print("\nResultado geometrico:")
print(f"- Area:      {ar:.2f} m2")
print(f"- Perimetro: {per:.2f} m")