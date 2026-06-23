import random
vidas_totales = 8
print(f'Tienes un total de {vidas_totales} intentos para adivinar el numero secreto.')

numero_secreto = random.randint(1, 20)
while True:
    intento = int(input('\nAdivina el numero del (1 al 20): '))
    
    if intento == numero_secreto:
        print('Felicidades adivinaste el numero secreto') 
        break
    
    vidas_totales = vidas_totales - 1
    
    if vidas_totales == 0:
        print('Lo sentimos, ya no te quedan intentos disponibles. Game Over gil.')
        print(f'El número secreto era: {numero_secreto}')
        break
        
    elif intento > numero_secreto:
        print('El numero secreto es menor, intenta de nuevo')
        print(f'Te quedan un total de {vidas_totales} intentos')
        
    elif intento < numero_secreto:
        print('El numero secreto es mayor, intente de nuevo')
        print(f'Te quedan un total de {vidas_totales} intentos')