def calcular_macronutrientes(peso, objetivo):
    """Calculadora de distribución básica de macronutrientes diarios"""
    if objetivo == "volumen":
        proteina_g = peso * 2.0
        grasa_g = peso * 1.0
        carbohidratos_g = peso * 4.5
    else:  # definicion
        proteina_g = peso * 2.4
        grasa_g = peso * 0.8
        carbohidratos_g = peso * 2.5

    return proteina_g, grasa_g, carbohidratos_g


print(f"\n{calcular_macronutrientes.__doc__}")

while True:
    try:
        peso = float(input("Ingrese su peso corporal en kg: "))
        if peso <= 35 or peso > 250:
            raise ValueError

        obj = input("Objetivo (volumen / definicion): ").strip().lower()
        if obj not in ("volumen", "definicion"):
            raise ValueError

        break
    except ValueError:
        print("ERROR: Peso fuera de rango o texto no reconocido ('volumen' o 'definicion').\n")

prot, gras, carb = calcular_macronutrientes(peso, obj)
print(f"\nResultado para {obj.capitalize()}:")
print(f"- Proteínas:     {prot:.1f} g")
print(f"- Grasas:        {gras:.1f} g")
print(f"- Carbohidratos: {carb:.1f} g")