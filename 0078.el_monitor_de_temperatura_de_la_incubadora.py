registro_de_temperaturas = []

for num_temperatura in range(1,6):
    while True:
        try:
            temperatura = float(input(f'Ingrese la temperatura de la zona {num_temperatura}:\n'))
            if temperatura <= 0:
                raise ValueError
            registro_de_temperaturas.append(temperatura)
            break
        except ValueError:
            print('ERROR: Dato incorrecto.')
            print('Intente de nuevo.')

zonas_frias = []
for s in registro_de_temperaturas:
    if s < 37.0:
        zonas_frias.append(s)

if len(registro_de_temperaturas) > 0:
    temp_promedio = sum(registro_de_temperaturas) / len(registro_de_temperaturas)
    num_zonas_defectuosas = len(zonas_frias)
    porcentaje_de_afectacion = (num_zonas_defectuosas / len(registro_de_temperaturas)) * 100
else:
    temp_promedio = 0.0
    num_zonas_defectuosas = 0.0
    porcentaje_de_afectacion = 0.0

print('\n----- MONITOREO DE TEMPERATURA DE LAS INCUBADORAS -----\n')
print(f'Lista original de todas las temperaturas: {registro_de_temperaturas}')
print(f'Lista filtrada de las temperaturas que estan bajas (menores a 37.0 C): {zonas_frias}')
print(f'Temperatura promedio: {temp_promedio:.2f}')
print(f'Porcentaje de afectacion: {porcentaje_de_afectacion:.1f}')

if porcentaje_de_afectacion > 20:
    print('🚨 ¡ALERTA DE SISTEMA! El porcentaje de zonas frías supera el 20%. Encendiendo calefactores de emergencia inmediatamente.')
else:
    print('✅ Clima de incubación estable. Temperatura bajo control.')