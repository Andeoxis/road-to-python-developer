def calcular_ica(cintura_cm, altura_cm):
    """Calculadora de Indice Cintura-Altura (ICA) para estimar riesgo cardiometabolico"""
    ica = cintura_cm / altura_cm
    riesgo = "Bajo riesgo" if ica < 0.50 else "Riesgo incrementado"
    return ica, riesgo


print(f"\n{calcular_ica.__doc__}")

while True:
    try:
        cintura = float(input("Circunferencia de cintura en cm: "))
        if cintura <= 30 or cintura > 200:
            raise ValueError

        altura = float(input("Estatura en cm: "))
        if altura <= 100 or altura > 250:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese medidas corporales logicas en centimetros.\n")

indice, estado = calcular_ica(cintura, altura)
print("\nResultado biometrico:")
print(f"- ICA obtenido: {indice:.2f}")
print(f"- Categoria:    {estado}")