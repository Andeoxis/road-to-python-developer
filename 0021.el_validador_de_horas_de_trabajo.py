# Estás programando un sistema de registro de asistencia para una empresa.
# Los empleados tienen que registrar cuántas horas trabajaron en un día.
# Por política de la empresa, un empleado no puede registrar menos de 1 hora al día,
# y tampoco puede registrar más de 12 horas por día (horas extras máximas permitidas).

registro_de_asistencias = int(input('Ingrese cuantas horas trabajo en un dia (del 1 al 12): '))

# CAMBIAMOS 'and' POR 'or'
while registro_de_asistencias < 1 or registro_de_asistencias > 12:
    print('Las horas que ingreso son incorrectas. Intente de nuevo papuchin.')
    registro_de_asistencias = int(input('Ingrese cuantas horas trabajo en un dia (del 1 al 12): '))

# Si sale del while, el número SÍ o SÍ está entre 1 y 12
sueldo_total = registro_de_asistencias * 40
print(f'Registro correcto. Tu sueldo por hoy es de {sueldo_total} Bs.')

if registro_de_asistencias >= 6:
    print('Perfecto, trabajaste de manera consciente.')
else:
    print('Tienes que mejorar esas horas amigo.')