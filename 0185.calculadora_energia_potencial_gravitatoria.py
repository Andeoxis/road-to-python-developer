def calcular_energia_potencial(masa, altura):
    """Calculadora de energia potencial gravitatoria en la Tierra (Ep = m * g * h)"""
    gravedad = 9.81
    energia = masa * gravedad * altura
    return energia


print(f"\n{calcular_energia_potencial.__doc__}")

while True:
    try:
        masa = float(input("Ingrese la masa en kg: "))
        if masa <= 0 or masa > 50000:
            raise ValueError

        altura = float(input("Ingrese la altura respecto al suelo en metros: "))
        if altura < 0 or altura > 10000:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Masa mayor a 0 y altura mayor o igual a 0.\n")

resultado = calcular_energia_potencial(masa, altura)
print("\nResultado:")
print(f"Energia potencial gravitatoria: {resultado:.2f} Joules")