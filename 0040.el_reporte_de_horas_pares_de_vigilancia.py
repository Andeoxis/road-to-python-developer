# Imagínate que en la incubadora de Cochabamba tienes un sensor térmico inteligente. Para no saturar el sistema con alertas a cada rato,
# el sensor solo hace un reporte general cada horas pares del día, cubriendo el turno fuerte que va desde las 06:00 de la mañana hasta las 22:00 de la noche.

# print('\n----------EL REPORTE DE HORAS PARES DE VIGILANCIA ----------\n')

# for reporte in range(6, 24, 2):
#     print(f'Hora {reporte}:00 -> Temperatura estable. Sensores OK.')

for reporte in range(20, -1, -1):
    print(f'Dia: {reporte} de 20')
print(f'Excelente llegaste al dia {reporte} felicidades.')