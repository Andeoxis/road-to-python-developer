def calcular_presupuesto_pintura(metros_cuadrados, manos, rendimiento_m2_litro, precio_litro):
    """Calculadora de litros necesarios y costo estimado para pintar una superficie"""
    superficie_total = metros_cuadrados * manos
    litros_necesarios = superficie_total / rendimiento_m2_litro
    costo_total = litros_necesarios * precio_litro
    return litros_necesarios, costo_total


print(f"\n{calcular_presupuesto_pintura.__doc__}")

while True:
    try:
        area = float(input("Area de la pared en m2: "))
        if area <= 0:
            raise ValueError

        manos = int(input("Numero de manos de pintura (1-5): "))
        if manos < 1 or manos > 5:
            raise ValueError

        rendimiento = float(input("Rendimiento de la pintura (m2 por litro, prom: 10): "))
        if rendimiento <= 0:
            raise ValueError

        precio = float(input("Precio por litro de pintura ($): "))
        if precio <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Verifique los valores ingresados (deben ser positivos y manos entre 1 y 5).\n")

litros, total = calcular_presupuesto_pintura(area, manos, rendimiento, precio)
print("\nPresupuesto:")
print(f"- Pintura requerida: {litros:.2f} litros")
print(f"- Costo estimado:    ${total:.2f}")