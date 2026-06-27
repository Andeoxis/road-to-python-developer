listos_para_venta = 0
bajos_de_peso = 0


for pollos in range(1, 6):
    peso = float(input('Ingrese el peso de su pollo: '))
    if peso >= 2.2:
        listos_para_venta += 1
        print(f'🐔 Pollo N°{pollos}: Aprobado! Peso excelente.')
    else:
        bajos_de_peso += 1
        print(f'⚠️ Pollo N° {pollos}: Alerta, bajo de peso. Requiere más alimento.')

print(f'''📊 --- BALANCE DE CARGA DEL GALPÓN ---

🚚 Total pollos listos para la venta: {listos_para_venta}

🌾 Total pollos que se quedan en engorde: {bajos_de_peso}''')