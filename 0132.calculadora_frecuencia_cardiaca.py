def calcular_zonas_cardiacas(edad):
    '''Calculadora cardiaca'''
    fcm = 208 - (0.7 * edad)
    zona_minima = fcm * 0.60
    zona_maxima = fcm * 0.70
    return fcm, zona_minima, zona_maxima

print(f'\n{calcular_zonas_cardiacas.__doc__}')

while True:
    try:
        eda = int(input('Ingrese su edad: '))
        if 12 < eda > 100:
            raise ValueError
        break
    except ValueError:
        print("ERROR: Ingrese una edad válida entre 12 y 100 años.\n")
fcm, z_min, z_max = calcular_zonas_cardiacas(eda)
print("\nResultado:")
print(f"- FCM estimada: {fcm:.0f} ppm")
print(f"- Zona quema de grasa (60%-70%): {z_min:.0f} a {z_max:.0f} ppm")