def calcular_presion_fluido(densidad_kg_m3, profundidad_m):
    """Calculadora de presion hidrostatica a una profundidad dada en un fluido"""
    gravedad = 9.81
    presion_pascales = densidad_kg_m3 * gravedad * profundidad_m
    presion_kpa = presion_pascales / 1000
    return presion_pascales, presion_kpa


print(f"\n{calcular_presion_fluido.__doc__}")

while True:
    try:
        densidad = float(input("Densidad del fluido en kg/m3 (ej: agua = 1000): "))
        if densidad <= 0 or densidad > 20000:
            raise ValueError

        profundidad = float(input("Profundidad en metros: "))
        if profundidad <= 0 or profundidad > 11000:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese valores positivos para densidad y profundidad.\n")

pa, kpa = calcular_presion_fluido(densidad, profundidad)
print("\nPresion calculada:")
print(f"- En Pascales:      {pa:.2f} Pa")
print(f"- En KiloPascales:  {kpa:.2f} kPa")