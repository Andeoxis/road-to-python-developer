texto = "python es genial y python es facil aprender python con practica constante"
contador_palabras = {}
palabras = texto.split()
for palabra in palabras:
    acumulado = contador_palabras.get(palabra, 0)
    contador_palabras[palabra] = acumulado + 1

print(contador_palabras)