def calcular_hipotenusa_catetos(cateto_a, cateto_b):
    """Calculadora de hipotenusa de un triangulo rectangulo mediante Teorema de Pitagoras"""
    hipotenusa = ((cateto_a ** 2) + (cateto_b ** 2)) ** 0.5
    return hipotenusa


print(f"\n{calcular_hipotenusa_catetos.__doc__}")

while True:
    try:
        a = float(input("Longitud del cateto A: "))
        b = float(input("Longitud del cateto B: "))
        if a <= 0 or b <= 0:
            raise ValueError
        break
    except ValueError:
        print("ERROR: Las longitudes deben ser numeros positivos mayores a 0.\n")

c = calcular_hipotenusa_catetos(a, b)
print("\nResultado trigonometrico:")
print(f"Hipotenusa calculada: {c:.2f}")