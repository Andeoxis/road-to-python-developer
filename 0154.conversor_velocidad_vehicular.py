def convertir_velocidad(valor_kmh):
    """Conversor de velocidad de km/h a metros por segundo (m/s) y millas por hora (mph)"""
    ms = valor_kmh / 3.6
    mph = valor_kmh * 0.621371
    return ms, mph


print(f"\n{convertir_velocidad.__doc__}")

while True:
    try:
        velocidad = float(input("Ingrese la velocidad en km/h: "))
        if velocidad < 0 or velocidad > 500:
            raise ValueError
        break
    except ValueError:
        print("ERROR: La velocidad debe ser un numero entre 0 y 500.\n")

metros_seg, millas_hora = convertir_velocidad(velocidad)
print("\nEquivalencias:")
print(f"- Metros por segundo: {metros_seg:.2f} m/s")
print(f"- Millas por hora:    {millas_hora:.2f} mph")