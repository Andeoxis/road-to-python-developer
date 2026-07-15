ventas = []
for i in range(1, 7):
    while True:
        try:
            precio_producto = int(input(f'Pon el precio del producto {i}:\n'))
            ventas.append(precio_producto)
            break
        except ValueError:
            print('ERROR: Solo debes colocara numeros, intenta de nuevo.')

suma_total = sum(ventas)
mas_caro = max(ventas)
mas_barato = min(ventas)
calculo_ganancia = suma_total * 0.7

print('\n---- CONTROL DE INVENTARIO ----')
print(f'El total de dinero ingresado es: {suma_total}.')
print(f'El producto mas caro vendido es: {mas_caro}.')
print(f'El producto mas barato vendido es: {mas_barato}.')
print(f'La ganancia final de la tienda es: {calculo_ganancia}.')

if calculo_ganancia >= 150:
    print('Excelente dia de ventas. Meta superada.')
else:
    print('Buen esfuerzo, pero hoy no se alcanzo la meta diaria.')

