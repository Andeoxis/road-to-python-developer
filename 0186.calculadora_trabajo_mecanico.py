def calcular_trabajo(fuerza, distancia):
    """Calculadora de trabajo mecanico lineal constante (W = F * d)"""
    trabajo = fuerza * distancia
    return trabajo


print(f"\n{calcular_trabajo.__doc__}")

while True:
    try:
        f = float(input("Ingrese la fuerza aplicada en Newtons (N): "))
        if f <= 0 or f > 100000:
            raise ValueError

        d = float(input("Ingrese el desplazamiento realizado en metros (m): "))
        if d <= 0 or d > 50000:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Tanto la fuerza como el desplazamiento deben ser mayores a 0.\n")

w = calcular_trabajo(f, d)
print("\nResultado:")
print(f"Trabajo mecanico efectuado: {w:.2f} Joules")