def convertir_almacenamiento(gigabytes, unidad_destino):
    """Conversor de almacenamiento binario desde Gigabytes (GB) a MB, KB o Bytes"""
    multiplicadores = {
        "mb": 1024,
        "kb": 1024 ** 2,
        "b": 1024 ** 3
    }
    valor_convertido = gigabytes * multiplicadores[unidad_destino]
    return valor_convertido


print(f"\n{convertir_almacenamiento.__doc__}")

while True:
    try:
        gb = float(input("Ingrese la cantidad en Gigabytes (GB): "))
        if gb <= 0:
            raise ValueError

        unidad = input("Seleccione la unidad destino (mb / kb / b): ").strip().lower()
        if unidad not in ("mb", "kb", "b"):
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese un tamaño positivo y una unidad permitida (mb, kb, b).\n")

resultado = convertir_almacenamiento(gb, unidad)
print("\nResultado:")
print(f"{gb:.2f} GB equivalen a: {resultado:,.0f} {unidad.upper()}")