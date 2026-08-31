while True:
    try:
        print('--- Ingrese sus notas de estudiante ---')
        nota1 = float(input('Ingrese nota 1: '))
        nota2 = float(input('Ingrese nota 2: '))
        nota3 = float(input('Ingrese nota 3: '))

        # Validación opcional: que las notas estén entre 0 y 100
        if not (0 <= nota1 <= 100 and 0 <= nota2 <= 100 and 0 <= nota3 <= 100):
            print('Error: Las notas deben estar entre 0 y 100.\n')
            continue

    except ValueError:
        print('Dato erróneo (solo ingrese números).\n')
        continue  # Reinicia el bucle sin ejecutar el cálculo

    # Solo llega aquí si las 3 notas fueron válidas
    promedio = (nota1 + nota2 + nota3) / 3
    print(f'\nTu promedio es de {promedio:.2f}')

    if promedio >= 61:
        print('Estado: Aprobado')
    elif 40 <= promedio < 61:
        print('Estado: Recuperatorio')
    else:
        print('Estado: Reprobado')
    
    break  # Finaliza el programa tras mostrar el resultado