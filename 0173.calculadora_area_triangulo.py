def calcular_area_triangulo(base, altura):
    """Calculadora de area de superficie de un triangulo plano"""
    area = (base * altura) / 2
    return area


print(f"\n{calcular_area_triangulo.__doc__}")

while True:
    try:
        b = float(input("Ingrese la base en metros: "))
        h = float(input("Ingrese la altura en metros: "))
        if b <= 0 or h <= 0:
            raise ValueError
        break
    except ValueError:
        print("ERROR: La base y la altura deben ser numeros mayores a cero.\n")

resultado = calcular_area_triangulo(b, h)
print("\nResultado:")
print(f"Area calculada: {resultado:.2f} m2")