registro_de_flexiones = []
for series_de_flexiones in range(1,6):
  while True:
    try:
      flexiones = int(input(f'Ingresa la serie N{series_de_flexiones} cuantas flexiones hiciste:\n'))
      if flexiones <= 0:
        raise ValueError
      registro_de_flexiones.append(flexiones)
      break
    except ValueError:
      print('ERROR: Dato erroneo.')
      print('Intenta de nuevo.')
      print()

pocas_flexiones = []
for s in registro_de_flexiones:
  if s < 5:
    pocas_flexiones.append(s)

if len(registro_de_flexiones) > 0:
  promedio = sum(registro_de_flexiones) / len(registro_de_flexiones)
  numero_pocas_flexiones = len(pocas_flexiones)
else:
  promedio = 0
  numero_pocas_flexiones = 0

print('\n----- REGISTRO DE FLEXIONES -----')
print(f'El numero total original de flexiones es: {registro_de_flexiones}')
print(f'El maximo numero de flexiones es: {max(registro_de_flexiones)}')
print(f'El minimo numero de flexiones es: {min(registro_de_flexiones)}')
print(f'El promedio de numero de flexiones es: {promedio}')
print(f'Series con menos de 5 flexiones: {numero_pocas_flexiones}')
print(f'La suma total de todas las flexiones es: {sum(registro_de_flexiones)}')