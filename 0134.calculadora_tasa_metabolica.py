def calcular_tmb(peso, altura_cm, edad, sexo):
    """Calculadora de Tasa Metabólica Basal (Fórmula Mifflin-St Jeor)"""
    tmb_base = (10 * peso) + (6.25 * altura_cm) - (5 * edad)
    if sexo == "m":
        return tmb_base + 5
    return tmb_base - 161


print(f"\n{calcular_tmb.__doc__}")

while True:
    try:
        sex = input("Ingrese su sexo biológico (m/f): ").strip().lower()
        if sex not in ("m", "f"):
            raise ValueError

        peso = float(input("Ingrese su peso en kg: "))
        if peso <= 30 or peso > 300:
            raise ValueError

        altura = float(input("Ingrese su altura en centímetros (ej: 175): "))
        if altura < 100 or altura > 250:
            raise ValueError

        edad = int(input("Ingrese su edad en años: "))
        if edad < 15 or edad > 100:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Verifique los datos ingresados y vuelva a intentar.\n")

calorias = calcular_tmb(peso, altura, edad, sex)
print("\nResultado:")
print(f"Tu gasto metabólico basal estimado es: {calorias:.0f} kcal/día")