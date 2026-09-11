def calcular_geometria_circulo(radio):
    """Calculadora de area y perimetro de una circunferencia"""
    pi = 3.141592653589793
    area = pi * (radio ** 2)
    perimetro = 2 * pi * radio
    return area, perimetro


print(f"\n{calcular_geometria_circulo.__doc__}")

while True:
    try:
        r = float(input("Ingrese el radio del circulo en metros: "))
        if r <= 0:
            raise ValueError
        break
    except ValueError:
        print("ERROR: El radio debe ser un numero positivo mayor a 0.\n")

area, perimetro = calcular_geometria_circulo(r)
print("\nPropiedades geometricas:")
print(f"- Area:      {area:.2f} m2")
print(f"- Perimetro: {perimetro:.2f} m")