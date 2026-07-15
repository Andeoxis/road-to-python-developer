notas =[]
for i in range(1, 6):
    while True:
        try:
            nota = int(input(f'Coloca aca tu nota estudiante N{i}:\n'))
            notas.append(nota)
            break
        except ValueError:
            print('ERROR. Solo coloca numeros, intenta de nuevo.')

notas.sort()
promedio = sum(notas) / 5
aprobados = 0
for n in notas:
    if n >= 51:
        aprobados += 1

reprobados = 5 - aprobados

print('\n---- REPORTE DE CALIFICACIONES ----')
print(f'Notas ordenadas de menor a mayor: {notas}')
print(f'Promedio del curso: {promedio} Puntos.')
print(f'Nota más baja: {min(notas)} | Nota más alta: {max(notas)}')
print(f'Cantidad de aprobados: {aprobados}')
print(f'Cantidad de reprobados: {reprobados}')
