print('n\---------- EL CLASIFICADO AUTOMOTIZADO DE HUEVOS (CONTROL DE CALILDAD) ----------\n')

huevos_descartados = 0
huevos_aprobados = 0

for numero_huevo in range(1, 30):
    if numero_huevo % 2 == 0:
        huevos_aprobados += 1
        print(f'🥚 Huevo N° {numero_huevo}: APROBADO para la venta.')
    else:
        huevos_descartados += 1
        print(f'🥚 Huevo N° {numero_huevo}: DESCARTADO para la venta.')
print(f'''📊 --- REPORTE DE CALIDAD ---
✅ Total Aprobados: {huevos_aprobados}
❌ Total Descartados: {huevos_descartados}''')