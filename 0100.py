while True:
    try:
        anos_exp = int(input('Ingrese sus anos de experiencia: \n'))
        if anos_exp < 0:
            raise ValueError

        nivel_de_ingles = input('Ingrese su nivel de ingles ("A"Avanzado, "I"Intermedio, "B"Basico):\n').lower().strip()
        if nivel_de_ingles not in ['a', 'i', 'b']:
            raise ValueError

        titulo_u = input('Usted tiene titulo universitario (S/N):\n').lower().strip()
        if titulo_u not in ['s', 'n']:
            raise ValueError

        break

    except ValueError:
        print('Error. Intente nuevamente.')

if anos_exp >= 5 and nivel_de_ingles == 'a' and titulo_u == 's':
    print('Usted es: Senior')
elif 3 <= anos_exp <= 4 and (nivel_de_ingles == 'a' or nivel_de_ingles == 'i'):
    print('Usted es: Mid-Level')
elif 1 <= anos_exp <= 2:
    print('Usted es: Junior')
else:
    print('Usted no es elegible.')