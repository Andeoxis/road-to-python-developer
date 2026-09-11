def calcular_autonomia_restante(capacidad_mah, consumo_ma):
    """Calculadora de tiempo estimado de duracion de bateria portatil"""
    horas_totales = capacidad_mah / consumo_ma
    horas = int(horas_totales)
    minutos = int((horas_totales - horas) * 60)
    return horas, minutos


print(f"\n{calcular_autonomia_restante.__doc__}")

while True:
    try:
        mah = float(input("Capacidad de la bateria en mAh: "))
        if mah <= 0:
            raise ValueError

        consumo = float(input("Consumo continuo del dispositivo en mA: "))
        if consumo <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Los valores de capacidad y consumo deben ser mayores a 0.\n")

hrs, mins = calcular_autonomia_restante(mah, consumo)
print("\nAutonomia estimada:")
print(f"Duracion: {hrs} horas y {mins} minutos")