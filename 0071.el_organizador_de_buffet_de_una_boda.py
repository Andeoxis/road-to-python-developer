pedidos = []
for i in range(1,6):
    while True:
        try:
            platos = str(input(f'Dame el nombre del plato N{i}:\n')).lower().strip()
            if platos == '' or platos.isdigit():
                raise ValueError
            pedidos.append(platos)
            break
        except ValueError:
            print('ERROR: Te equivocaste en el dato, intenta de nuevo.')

platos_sin_repetir = list(set(pedidos))
numero_de_platos_sin_repetir = len(platos_sin_repetir)
pedido_especial = 'planchita' in platos_sin_repetir

print('\n----- REPORTE DEL CATERING -----')
print(f'Pedidos originales: {pedidos}')
print(f'Platos unicos a preparar: {platos_sin_repetir}')
print(f'Total de platos diferentes: {numero_de_platos_sin_repetir}')
print(50 * '-')

if pedido_especial:
    print('Se pidio el pedido especial.')
else:
    print('No se pidio el pedido especial.')