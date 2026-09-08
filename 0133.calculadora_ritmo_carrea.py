def calcular_ritmo(distancia_km, minutos, segundos):
    """Calculadora de ritmo de carrera (pace por km)"""
    tiempo_total_minutos = minutos + (segundos / 60)
    ritmo_decimal = tiempo_total_minutos / distancia_km
    ritmo_min = int(ritmo_decimal)
    ritmo_seg = int((ritmo_decimal - ritmo_min) * 60)
    return ritmo_min, ritmo_seg


print(f"\n{calcular_ritmo.__doc__}")

while True:
    try:
        dist = float(input("Ingrese la distancia recorrida en km: "))
        if dist <= 0 or dist > 100:
            raise ValueError

        minutos = int(input("Ingrese los minutos empleados: "))
        if minutos < 0 or minutos > 300:
            raise ValueError

        segundos = int(input("Ingrese los segundos empleados (0-59): "))
        if segundos < 0 or segundos >= 60:
            raise ValueError

        if minutos == 0 and segundos == 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese valores válidos (distancia > 0 y tiempo real).\n")

ritmo_min, ritmo_seg = calcular_ritmo(dist, minutos, segundos)
print("\nResultado:")
print(f"Tu ritmo medio es: {ritmo_min}:{ritmo_seg:02d} min/km")