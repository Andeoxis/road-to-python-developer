def calcular_mesualidad(edad, disiplina):
    disiplina_limpia = disiplina.lower().strip()
    if disiplina_limpia == 'gimnasio':
        return 200
    elif disiplina_limpia == 'voleibol':
        if edad < 18:
            return 144
        return 180
    return 'Dato erroneo'

edadd = int(input('Ingresa tu edad: '))
disiplinaa = input('Ingresa la disiplina (gimnasio/voleibol): ')

edad_disiplina = calcular_mesualidad(edadd, disiplinaa)

if edad_disiplina == 'Dato erroneo':
    print(f'ERROR: La diciplina ingresada no existe.')
else:
    print(f'El monto a pagar es de {edad_disiplina}')
