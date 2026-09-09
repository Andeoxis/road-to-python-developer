def calcular_tiempo_descarga(tamano_gb, velocidad_mbps):
    """Calculadora de tiempo estimado de descarga de archivos"""
    megabits = tamano_gb * 1024 * 8
    segundos_totales = megabits / velocidad_mbps
    minutos = int(segundos_totales // 60)
    segundos = int(segundos_totales % 60)
    return minutos, segundos


print(f"\n{calcular_tiempo_descarga.__doc__}")

while True:
    try:
        tamano = float(input("Ingrese el tamano del archivo en GB: "))
        if tamano <= 0 or tamano > 2000:
            raise ValueError

        velocidad = float(input("Ingrese la velocidad de descarga en Mbps: "))
        if velocidad <= 0 or velocidad > 5000:
            raise ValueError

        break
    except ValueError:
        print("ERROR: El tamano y la velocidad deben ser valores positivos.\n")

mins, segs = calcular_tiempo_descarga(tamano, velocidad)
print("\nResultado:")
print(f"Tiempo estimado: {mins} min {segs:02d} seg")