def calcular_capacidad_peces(largo_cm, ancho_cm, alto_cm):
    """Calculadora de volumen de acuario y capacidad recomendada de peces pequenos"""
    litros = (largo_cm * ancho_cm * alto_cm) / 1000
    peces_maximos = int(litros // 4)
    return litros, peces_maximos


print(f"\n{calcular_capacidad_peces.__doc__}")

while True:
    try:
        largo = float(input("Largo de la pecera en cm: "))
        ancho = float(input("Ancho de la pecera en cm: "))
        alto = float(input("Alto de la pecera en cm: "))
        if largo <= 0 or ancho <= 0 or alto <= 0:
            raise ValueError
        break
    except ValueError:
        print("ERROR: Todas las dimensiones deben ser numeros positivos.\n")

vol_lts, max_peces = calcular_capacidad_peces(largo, ancho, alto)
print("\nResultado:")
print(f"- Capacidad del acuario: {vol_lts:.1f} litros")
print(f"- Peces pequenos recomendados (regla 4L/pez): {max_peces} ejemplares")