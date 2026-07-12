total = 0

for i in range(1, 4):
    
    while True:
        try:
            producto = int(input(f'Ingrese el precio del producto {i}:\n'))
            total += producto
            print('Producto ingresado con éxito.\n')
            break  
        except ValueError:
            print('ERROR: Solo ingresa números, no letras. Intenta de nuevo con este producto.\n')

print("--- RESUMEN DE COMPRA ---")
if total >= 100:
    total_final = total * 0.9
    print(f'¡Felicidades! Aplica descuento del 10%.')
    print(f'Total original: {total} Bs')
    print(f'El total con descuento es: {total_final} Bs')
else:
    print(f'El total es {total} Bs (No aplica descuento de promoción).')