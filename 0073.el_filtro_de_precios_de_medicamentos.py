precios = []
for i in range(1,6):
    while True:
        try:
            medicamentos = float(input(f'Dame el precio del medicamento N{i}:\n'))
            if medicamentos < 0:
                raise ValueError
            precios.append(medicamentos)
            break
        except ValueError:
            print('ERROR: Pusiste un dato erroneo, intenta de nuevo.')

precios_validos = []
for p in precios:
    if p > 0.0:
        precios_validos.append(p)

if len(precios_validos) > 0:
    promedio = sum(precios_validos) / len(precios_validos)
    max_precio = max(precios_validos)
    min_precio = min(precios_validos)
    numero_especial = 50.0 in precios_validos
else:
    promedio = 0.0
    max_precio = 0.0
    min_precio = 0.0
    numero_especial = False

print('\n----- PRECIOS DE MEDICAMENTOS =====\n')
print(f'Esta es la lista limpia sin los 0.0: {precios_validos}')
print(f'Este es el promedio: {promedio:.2f}')
print(f'Este es el precio maximo {max_precio} y este es el precio minimo {min_precio}')
if numero_especial:
    print('Si, tenemos un medicamento en el inventario con el precio exacto de 50.0 Bs.')
else:
    print('No se encontraron medicamentos con el precio de 50.0 Bs.')
