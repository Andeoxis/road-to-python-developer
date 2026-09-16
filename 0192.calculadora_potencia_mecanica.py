def calcular_potencia(trabajo_joules, tiempo_segundos):
    """Calculadora de potencia mecanica en Watts y Caballo de Fuerza (HP)"""
    potencia_w = trabajo_joules / tiempo_segundos
    potencia_hp = potencia_w / 745.7
    return potencia_w, potencia_hp


print(f"\n{calcular_potencia.__doc__}")

while True:
    try:
        w = float(input("Trabajo realizado en Joules (J): "))
        if w <= 0:
            raise ValueError

        t = float(input("Tiempo empleado en segundos (s): "))
        if t <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese valores de trabajo y tiempo mayores a cero.\n")

watts, hp = calcular_potencia(w, t)
print("\nPotencia desarrollada:")
print(f"- En Watts:                {watts:.2f} W")
print(f"- En Caballos de Fuerza:   {hp:.3f} HP")