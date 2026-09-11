def calcular_duracion_lectura(palabras_totales, palabras_por_minuto):
    """Calculadora de tiempo de lectura en minutos y horas estimadas"""
    minutos_totales = palabras_totales / palabras_por_minuto
    horas = int(minutos_totales // 60)
    minutos_restantes = int(minutos_totales % 60)
    return horas, minutos_restantes


print(f"\n{calcular_duracion_lectura.__doc__}")

while True:
    try:
        palabras = int(input("Numero de palabras del documento/libro: "))
        if palabras <= 0:
            raise ValueError

        ppm = int(input("Velocidad de lectura (palabras por minuto, prom: 200): "))
        if ppm <= 0 or ppm > 1000:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese valores enteros positivos dentro de rangos normales.\n")

hrs, mins = calcular_duracion_lectura(palabras, ppm)
print("\nResultado:")
print(f"Tiempo estimado de lectura: {hrs} horas y {mins} minutos")