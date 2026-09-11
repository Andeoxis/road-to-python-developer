def calcular_calorias_totales(proteinas_g, carbohidratos_g, grasas_g):
    """Calculadora de aporte energetico total a partir de macronutrientes"""
    cal_prot = proteinas_g * 4
    cal_carb = carbohidratos_g * 4
    cal_grasa = grasas_g * 9
    total_kcal = cal_prot + cal_carb + cal_grasa
    return total_kcal


print(f"\n{calcular_calorias_totales.__doc__}")

while True:
    try:
        prot = float(input("Proteinas (gramos): "))
        carb = float(input("Carbohidratos (gramos): "))
        gras = float(input("Grasas (gramos): "))
        if prot < 0 or carb < 0 or gras < 0:
            raise ValueError
        if prot == 0 and carb == 0 and gras == 0:
            raise ValueError
        break
    except ValueError:
        print("ERROR: Ingrese valores numericos mayores o iguales a cero.\n")

calorias = calcular_calorias_totales(prot, carb, gras)
print("\nResultado nutricional:")
print(f"Energia aportada: {calorias:.1f} kcal")