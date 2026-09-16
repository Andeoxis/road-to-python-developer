def calcular_calor_transferido(masa_kg, calor_esp, delta_temp):
    """Calculadora de calor sensible transferido (Q = m * c * DeltaT)"""
    calor_joules = masa_kg * calor_esp * delta_temp
    calor_kj = calor_joules / 1000
    return calor_joules, calor_kj


print(f"\n{calcular_calor_transferido.__doc__}")

while True:
    try:
        m = float(input("Masa de la sustancia en kg: "))
        if m <= 0 or m > 10000:
            raise ValueError

        c = float(input("Calor especifico en J/(kg*C) (ej: agua = 4184): "))
        if c <= 0:
            raise ValueError

        dt = float(input("Variacion de temperatura en grados Celsius (Delta T): "))
        if dt == 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: La masa y calor especifico deben ser > 0, y el cambio termico distinto de 0.\n")

q_j, q_kj = calcular_calor_transferido(m, c, dt)
print("\nEnergia termica:")
print(f"- Calor transferido: {q_j:.2f} J")
print(f"- Equivalente en kJ: {q_kj:.2f} kJ")