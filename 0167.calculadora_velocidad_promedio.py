def calcular_velocidad_media(distancia_km, tiempo_horas):
    """Calculadora de velocidad promedio y ritmo medio de viaje"""
    velocidad = distancia_km / tiempo_horas
    minutos_por_km = (tiempo_horas * 60) / distancia_km
    return velocidad, minutos_por_km


print(f"\n{calcular_velocidad_media.__doc__}")

while True:
    try:
        dist = float(input("Distancia recorrida en km: "))
        if dist <= 0:
            raise ValueError

        tiempo = float(input("Tiempo total invertido en horas (ej: 1.5): "))
        if tiempo <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: La distancia y el tiempo deben ser numeros mayores a 0.\n")

vel_prom, ritmo = calcular_velocidad_media(dist, tiempo)
print("\nMetricas de viaje:")
print(f"- Velocidad media: {vel_prom:.2f} km/h")
print(f"- Ritmo medio:     {ritmo:.2f} min/km")