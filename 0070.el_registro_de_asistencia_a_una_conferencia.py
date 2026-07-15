asistencia = []
for i in range(1, 6):
    while True:
        try:
            CI = int(input(f'Coloca tu numero de CI numero N{i}:\n'))
            asistencia.append(CI)
            break
        except ValueError:
            print('ERROR: Solo debes colocar numeros, intenta de nuevo.')

asistentes_unicos = list(set(asistencia))

total_asistentes = len(asistentes_unicos)

asistio_especifico = 12345 in asistentes_unicos

print('\n---- REPORTE DE ASISTENCIA ----')
print(f'Registros originales: {asistencia}')
print(f'Lista limpia de asistentes (sin repetidos): {asistentes_unicos}')
print(f'Total de personas reales que asistieron: {total_asistentes}')
print('-------------------------------')

if asistio_especifico:
    print('El estudiante con CI 12345 SI asistio al evento.')
else:
    print('El estudiante con CI 12345 NO asistio al evento.')