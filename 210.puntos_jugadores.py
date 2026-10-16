partidos = [
    ("Carlos", 15),
    ("Mateo", 22),
    ("Carlos", 10),
    ("Sofia", 30),
    ("Mateo", 8),
    ("Carlos", 12),
    ("Sofia", 15),
    ("Daniel", 18)
]
tabla_posiciones = {}
for jugador, puntos in partidos:
    acumulado_anterior = tabla_posiciones.get(jugador, 0)
    tabla_posiciones[jugador] = acumulado_anterior + puntos
print(tabla_posiciones)