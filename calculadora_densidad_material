def calcular_densidad(masa_kg, volumen_m3):
    """Calculadora de densidad volumetrica para clasificacion de materiales"""
    densidad = masa_kg / volumen_m3
    return densidad


print(f"\n{calcular_densidad.__doc__}")

while True:
    try:
        masa = float(input("Ingrese la masa del material en kg: "))
        if masa <= 0 or masa > 100000:
            raise ValueError

        volumen = float(input("Ingrese el volumen ocupado en m3: "))
        if volumen <= 0 or volumen > 5000:
            raise ValueError

        break
    except ValueError:
        print("ERROR: La masa y el volumen deben ser valores mayores a cero.\n")

resultado = calcular_densidad(masa, volumen)
print("\nResultado:")
print(f"Densidad calculada: {resultado:.2f} kg/m3")