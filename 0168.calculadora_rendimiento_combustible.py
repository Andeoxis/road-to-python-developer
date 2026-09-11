def calcular_eficiencia_vehiculo(kilometros, litros_cargados):
    """Calculadora de eficiencia de consumo vehicular en km/l y l/100km"""
    km_por_litro = kilometros / litros_cargados
    litros_por_cien = (litros_cargados / kilometros) * 100
    return km_por_litro, litros_por_cien


print(f"\n{calcular_eficiencia_vehiculo.__doc__}")

while True:
    try:
        km = float(input("Kilometros recorridos desde la ultima carga: "))
        if km <= 0:
            raise ValueError

        litros = float(input("Litros consumidos/cargados: "))
        if litros <= 0:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Los valores de distancia y litros deben ser positivos.\n")

kml, l100 = calcular_eficiencia_vehiculo(km, litros)
print("\nRendimiento calculado:")
print(f"- Eficiencia: {kml:.2f} km/l")
print(f"- Consumo:    {l100:.2f} l/100km")