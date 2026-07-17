inventario = []

for numero_de_tonelada in range(1, 6):
    while True:
        try:
            toneladas = float(input(f'Ingrese el peso de la tonelada {numero_de_tonelada}:\n'))
            if toneladas < 0:
                raise ValueError
            inventario.append(toneladas)
            break
        except ValueError:
            print('ERROR: Ingrese un dato valido.')
            print('Intente de nuevo.')
print()
stock_critico = []
for s in inventario:
    if s < 1.5:
        stock_critico.append(s)

if len(inventario) > 0:
    promedio = sum(inventario) / len(inventario)
    cantidad_criticos = len(stock_critico)
    porcentaje_de_riesgo = ((cantidad_criticos) / len(inventario)) * 100
else:
    promedio = 0.0
    cantidad_criticos = 0.0
    porcentaje_de_riesgo = 0.0

print('\n----- REPORTE DE CONTROL DE STOCK -----')
print(f'Inventario registrado (toneladas): {inventario}')
print(f'Stocks en estado crítico (menos de 1.5 Tn): {stock_critico}')
print(f'Stock promedio del almacén: {promedio:.2f} Tn.')
print(f'Porcentaje de productos en riesgo: {porcentaje_de_riesgo:.1f}%')
print(50 * '-')
if porcentaje_de_riesgo > 40:
    print('ALERTA ROJA! Mas del 40% del almacen tiene stock critico. Realiza pedidos inmediatamente.')
else:
    print(f'Estado del almacen estable. Stock bajo control.')