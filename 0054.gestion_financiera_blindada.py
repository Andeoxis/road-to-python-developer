suma_de_montos = 0 #ok
promedio_de_dinero = 0 #ok
registro_con_exito = 0 #ok
registro_sin_exito = 0 #ok
numero_mas_grande = 0 #ok
for i in range(1, 11):
    while True:
        try:
            dinero_recibido = int(input(f'Semana {i}: Ingresa el monto de dinero que recibiste: '))
            break
        except ValueError:
            print('Error: Por favor, ingrese solo numeros enteros, no letras.\nIntentalo de nuevo...')
    if dinero_recibido > 0:
        print('Dinero registrado con exito.')
        registro_con_exito += 1
        suma_de_montos += dinero_recibido
        promedio_de_dinero = suma_de_montos / registro_con_exito
        if numero_mas_grande < dinero_recibido:
            numero_mas_grande = dinero_recibido
            print(f'Hasta ahora este es el numero mas grande: {numero_mas_grande}')
    else:
        print('Error. Dinero no registrado.')
        registro_sin_exito += 1
    print()
print(f'''Dinero registrado con exito son: {registro_con_exito}. La suma de los montos es: {suma_de_montos}. El numero mas grande es: {numero_mas_grande}. El promedio es: {promedio_de_dinero:.2f}.
Dinero no registrado son: {registro_sin_exito}

      ''')

    

