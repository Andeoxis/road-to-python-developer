pollos_premium = 0
sumados_el_peso = 0
for cantidad_de_pollos in range(1, 5):
    peso = float(input(f'Ingresa cuanto pesa el pollo N{cantidad_de_pollos}: '))
    if peso >= 2.5:
        pollos_premium += 1
        sumados_el_peso += peso
        print(f'Pollo numero {cantidad_de_pollos} añadido al lote primium.')
        print()
    else:
        print(f'Pollo numero {cantidad_de_pollos} se queda en lote estandar.')
        print()


print(f'Cantidad de pollos premium: {pollos_premium}')
if pollos_premium > 0:
    promedio = sumados_el_peso / pollos_premium
    print(f'El peso promedio del lote premium es de: {promedio:.2f}kilos.')
else:
    print('No se registraron pollos premium hoy para sacar promedio')

