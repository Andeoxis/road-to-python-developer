def calcular_peso_newtons(masa_kg, planeta):
    """Calculadora de peso en Newtons segun la gravedad de distintos astros"""
    gravedades = {
        "tierra": 9.81,
        "luna": 1.62,
        "marte": 3.71,
        "jupiter": 24.79
    }
    gravedad = gravedades[planeta]
    fuerza_n = masa_kg * gravedad
    return gravedad, fuerza_n


print(f"\n{calcular_peso_newtons.__doc__}")

while True:
    try:
        masa = float(input("Ingrese la masa del cuerpo en kg: "))
        if masa <= 0 or masa > 50000:
            raise ValueError

        cuerpo = input("Seleccione el astro (tierra / luna / marte / jupiter): ").strip().lower()
        if cuerpo not in ("tierra", "luna", "marte", "jupiter"):
            raise ValueError

        break
    except ValueError:
        print("ERROR: Masa mayor a 0 y astro valido de la lista.\n")

g, newtons = calcular_peso_newtons(masa, cuerpo)
print(f"\nFuerza en {cuerpo.capitalize()}:")
print(f"- Gravedad local: {g:.2f} m/s2")
print(f"- Peso ejercido:  {newtons:.2f} N")