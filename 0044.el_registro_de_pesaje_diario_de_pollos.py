peso_total = 0

for numero_de_pollo in range(1, 5):
    peso_actual = float(input(f'Ingrese el peso del Pollo N° {numero_de_pollo} en kilos: '))
    peso_total += peso_actual
print(f'''📊 Reporte del Galpón:
⚖️ El peso promedio de este lote es de: {peso_total / numero_de_pollo} kilos, papuchin.''')