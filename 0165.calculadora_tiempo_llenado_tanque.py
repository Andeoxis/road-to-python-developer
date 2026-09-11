def calcular_tiempo_llenado(capacidad_litros, caudal_litros_min):
    """Calculadora de tiempo de llenado de un reservorio hidraulico"""
    minutos_totales = capacidad_litros / caudal_litros_min
    horas = int(minutos_totales // 60)
    minutos = int(minutos_totales % 60)
    return horas, minutos


print(f"\n{calcular_tiempo_llenado.__doc__}")

while True:
    try:
        litros = float(input("Capacidad total del tanque (litros): "))
        if litros <= 0:
            raise ValueError

        caudal = float(input("Caudal de llenado (litros por minuto): "))
        if caudal <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese capacidades y caudales mayores a cero.\n")

hrs, mins = calcular_tiempo_llenado(litros, caudal)
print("\nResultado:")
print(f"Tiempo estimado de llenado: {hrs} h y {mins} min")