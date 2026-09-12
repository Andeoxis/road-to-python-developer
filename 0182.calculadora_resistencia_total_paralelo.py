def calcular_resistencias_paralelo(resistencia_1, resistencia_2):
    """Calculadora de resistencia electrica equivalente para dos resistores en paralelo"""
    resistencia_equivalente = (resistencia_1 * resistencia_2) / (resistencia_1 + resistencia_2)
    return resistencia_equivalente


print(f"\n{calcular_resistencias_paralelo.__doc__}")

while True:
    try:
        r1 = float(input("Valor de la resistencia 1 (Ohms): "))
        r2 = float(input("Valor de la resistencia 2 (Ohms): "))
        if r1 <= 0 or r2 <= 0:
            raise ValueError
        break
    except ValueError:
        print("ERROR: Los valores de resistencia deben ser positivos mayores a 0.\n")

r_total = calcular_resistencias_paralelo(r1, r2)
print("\nResultado:")
print(f"Resistencia equivalente (Req): {r_total:.2f} Ω")