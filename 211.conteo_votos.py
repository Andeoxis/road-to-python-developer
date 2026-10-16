votos = [
    "Python",
    "C++",
    "Python",
    "JavaScript",
    "Python",
    "C++",
    "Python",
    "JavaScript",
    "JavaScript",
    "Python"
]
conteo = {}
for voto in votos:
    acumulado = conteo.get(voto, 0)
    conteo[voto] = acumulado + 1
print(conteo)