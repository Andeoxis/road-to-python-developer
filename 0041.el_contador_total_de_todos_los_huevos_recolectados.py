# Imagina que en tu negocio tienes un pabellón con 5 nidos mecánicos inteligentes.
# El sistema pasa recolectando los huevos nido por nido, y necesitas saber cuántos huevos se juntaron en total al final del recorrido.

total_huevos = 0

for numero_nido in range(1, 6):
    total_huevos += 12
    print(f'Nido N*{numero_nido} revisado. Se sumaron 12 huevos al canasto. ')
print(f'📊 Reporte Final: Se recolectaron un total de {total_huevos} huevos hoy, papuchin.')
