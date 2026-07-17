lote_harina = []

for numero_de_peso_de_harina in range(1,6):
    while True:
        try:
            peso_de_arina = float(input(f'Ingrese el peso del paquete de harina N{numero_de_peso_de_harina}:\n'))
            if peso_de_arina <= 0:
                raise ValueError
            lote_harina.append(peso_de_arina)
            break
        except ValueError:
            print('ERROR: Dato erroneo.')
            print('Intente de nuevo.')

pesos_bajos = []
for s in lote_harina:
    if s < 0.95:
        pesos_bajos.append(s)

if len(lote_harina) > 0:
    promedio = sum(lote_harina) / len(lote_harina)
    paquetes_defectuosos = len(pesos_bajos)
    porcentaje_de_fallo = (paquetes_defectuosos / len(lote_harina)) * 100
else:
    promedio = 0.0
    paquetes_defectuosos = 0.0
    porcentaje_de_fallo = 0.0

print('\n----- REPORTE DE CONTROL -----')
print(f'Lista original de todos los pesos registrados es: {lote_harina}')
print(f'Lista filtrada con los pesos que resultaron ser bajos: {pesos_bajos}')
print(f'El peso promedio del lote es: {promedio:.2f}')
print(f'El porcentaje del fallo es: {porcentaje_de_fallo:.1f}')
if porcentaje_de_fallo > 20:
    print('ALERTA DE MAQUINA! El porcentaje de fallo supera el 20%. Calibrar la llenadora inmediatamente.')
else:
    print('Lote aprobado. La calibracion de la maquina esta estable.')
