def calculadora_de_calorias(proteinas, carbohidratos, grasas):
    '''Calcula el total de kilocalorias en base a los macronutrientes.'''
    return (proteinas * 4) + (carbohidratos * 4) + (grasas * 9)

print(f'\n{calculadora_de_calorias.__doc__}')

while True:
    try:
        
        protes = float(input('Ingrese la cantidad de proteinas: '))
        carbos = float(input('Ingrese la cantidad de carbohidratos: '))
        grasas = float(input('Ingrese la cantidad de grasas: '))

        if protes < 0 or carbos < 0 or grasas < 0:
            raise ValueError
        break

    except ValueError:
        print('Error: Ingrese valores numéricos válidos mayores o iguales a 0.\n')        

total = calculadora_de_calorias(protes, carbos, grasas)
print(f'Resultado: {total:.1f} kcal')