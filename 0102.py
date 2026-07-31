tipo_de_entrada = input('Ingrese el tipo de entrada (1.Nino, 2.Adulto, 3.Adulto Mayor):\n').lower().strip()
if tipo_de_entrada not in ['1', '2', '3']:
    print('Error')
    exit()

match tipo_de_entrada:
    case '1':
        print('Tu entrada es para nino')
        costo = 30
    case '2':
        print('Tu entrada es para adulto')
        costo = 40
    case '3':
        print('Tu entrada es para Adulto Mayor')
        costo = 50
    case '_':
        print('ERROR. Opcion no valida.')
        exit()

dia_de_la_semana = input('Ingrese el dia de la semana: (Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo)\n').lower().strip()
if dia_de_la_semana not in ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']:
    print('Error')
    exit()

if dia_de_la_semana == 'miercoles':
    total = costo * 0.80
    print(f'Tienes un descuento. Pagas un total de: {total}')
else:
    print(f'Usted paga {costo}')
    print('Usted no tiene descuento.')
    

