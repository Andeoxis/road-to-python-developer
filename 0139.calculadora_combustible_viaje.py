def calcular_costo_viaje(distancia_km, consumo_por_100km, precio_litro):
    """Calculadora de consumo y gasto de combustible para viajes en carretera"""
    litros_necesarios = (distancia_km / 100) * consumo_por_100km
    costo_total = litros_necesarios * precio_litro
    return litros_necesarios, costo_total


print(f"\n{calcular_costo_viaje.__doc__}")

while True:
    try:
        dist = float(input("Ingrese la distancia del trayecto en km: "))
        if dist <= 0 or dist > 10000:
            raise ValueError

        consumo = float(input("Ingrese el consumo medio del vehículo (litros/100km): "))
        if consumo <= 0 or consumo > 40:
            raise ValueError

        precio = float(input("Ingrese el precio del combustible por litro ($): "))
        if precio <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Los valores de distancia, consumo y precio deben ser mayores a 0.\n")

litros, total = calcular_costo_viaje(dist, consumo, precio)
print("\nResultado del trayecto:")
print(f"- Combustible estimado: {litros:.2f} litros")
print(f"- Costo total del viaje: ${total:.2f}")