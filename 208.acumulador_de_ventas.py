ventas_dia = [
    ("manzanas", 5),
    ("platanos", 2),
    ("manzanas", 3),
    ("naranjas", 10),
    ("platanos", 4),
    ("manzanas", 2),
    ("naranjas", 5)
]

totales = {}

for producto, cantidad in ventas_dia:
    # 1. Buscamos cuánto hay acumulado de ese producto (si no existe, da 0)
    acumulado_anterior = totales.get(producto, 0)
    
    # 2. Guardamos la suma en la clave de ese producto
    totales[producto] = acumulado_anterior + cantidad

print(totales)