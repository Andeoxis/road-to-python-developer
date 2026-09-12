def calcular_tiempo_subida(tamano_mb, velocidad_kbps):
    """Calculadora de tiempo de carga/subida en base a tasa de transferencia en Kbps"""
    kilobits_totales = tamano_mb * 1024 * 8
    segundos_totales = kilobits_totales / velocidad_kbps
    minutos = int(segundos_totales // 60)
    segundos = int(segundos_totales % 60)
    return minutos, segundos


print(f"\n{calcular_tiempo_subida.__doc__}")

while True:
    try:
        peso_mb = float(input("Tamano del archivo a subir en Megabytes (MB): "))
        if peso_mb <= 0:
            raise ValueError

        tasa_kbps = float(input("Velocidad de subida en Kbps: "))
        if tasa_kbps <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese valores estrictamente mayores a cero.\n")

minutos, segs = calcular_tiempo_subida(peso_mb, tasa_kbps)
print("\nResultado:")
print(f"Tiempo estimado de subida: {minutos} min {segs:02d} seg")