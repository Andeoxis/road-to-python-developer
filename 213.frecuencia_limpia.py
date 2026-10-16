parrafo = "Python es genial, Python es rapido. Aprender python requiere practica y constancia con python."
palabras = parrafo.lower().replace(',', '').replace('.', '').split()

diccionario = {}
for palabra_veces in palabras:
    acumulador = diccionario.get(palabra_veces, 0)
    diccionario[palabra_veces] = acumulador + 1

for clave, valor in diccionario.items():
    print(f"Etiqueta: {clave} -> Total: {valor}")