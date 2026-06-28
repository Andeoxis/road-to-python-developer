peso_max = 0
peso_min = 0
peso_med = 0
pollo_mas_grande = 0
for numero_de_pollo in range(1, 5):
    peso =  float(input(f'Ingrese el peso de pollo N {numero_de_pollo}: '))
    if peso > pollo_mas_grande:
        pollo_mas_grande = peso
    if peso >= 3:
        peso_max += 1
        print(f'Este es el primer super pollo {numero_de_pollo}.')
    elif 2 <= peso < 3:
        peso_med += 1
        print(f'Este es un pollo promedio {numero_de_pollo}')
    else:
        peso_min += 1
        print(f'Este es un pollo pequeno {numero_de_pollo}')

print(f'Escogiste un total de {peso_max} super pollos\nEscogiste un total de {peso_med} pollos promedio\nEscogiste un total de {peso_min} pollos pequenos')
print(f'Tienes un total de {numero_de_pollo} pollos.')
print(f'El pollo mas grande es {pollo_mas_grande}')
              
    