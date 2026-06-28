pollo_mas_pesado = 0
pollos_eficientes = 0
pollos_lentos = 0
for numero_de_pollos in range(1, 6):
    peso = float(input(f'Ingrese el peso del pollo N {numero_de_pollos}: '))
    if peso > pollo_mas_pesado:
        pollo_mas_pesado = peso
    if peso >= 2.3:
        pollos_eficientes += 1
    else:
        pollos_lentos += 1

porcentaje_eficiente = (pollos_eficientes / numero_de_pollos) * 100
porcentaje_lentos = (pollos_lentos / numero_de_pollos) * 100

print(f'''📊 --- ANALÍTICA DE RENDIMIENTO DEL LOTE ---

👑 El pollo más pesado del experimento registró: {pollo_mas_pesado:.2f}kilos.

🟢 Pollos Eficientes: {porcentaje_eficiente:.2f}% del lote.

🔴 Pollos Lentos: {porcentaje_lentos:.2f}% del lote.''')