def calcular_dilatacion(longitud_inicial, coef_alfa, variacion_temp):
    """Calculadora de dilatacion termica lineal de solidos (DeltaL = L0 * alfa * DeltaT)"""
    delta_l = longitud_inicial * coef_alfa * variacion_temp
    longitud_final = longitud_inicial + delta_l
    return delta_l, longitud_final


print(f"\n{calcular_dilatacion.__doc__}")

while True:
    try:
        l0 = float(input("Longitud inicial de la barra en metros: "))
        if l0 <= 0:
            raise ValueError

        alfa = float(input("Coeficiente de dilatacion lineal (ej: acero = 0.000012): "))
        if alfa <= 0:
            raise ValueError

        dt = float(input("Incremento o cambio de temperatura en C: "))
        if dt <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Todos los parametros deben ser valores positivos mayores a cero.\n")

cambio_longitud, long_total = calcular_dilatacion(l0, alfa, dt)
print("\nResultado termico:")
print(f"- Expansion lineal: {cambio_longitud:.6f} m")
print(f"- Longitud final:    {long_total:.6f} m")