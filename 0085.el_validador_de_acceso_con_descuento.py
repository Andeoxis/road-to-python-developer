def calcular_tarifa(horas_estacionamiento):
    costo_base = horas_estacionamiento * 10
    if horas_estacionamiento > 5:
        return costo_base - 15
    else:
        return costo_base

horas_quedadas = int(input('Ingresa cuantas horas se quedo: '))
costo_a_pagar = calcular_tarifa(horas_quedadas)
print(f'El monto final a pagar es de: {costo_a_pagar}')
