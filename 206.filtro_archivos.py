archivos_subidos = [
    "  main.py  ",
    "NOTAS.TXT",
    "   ",
    "MAIN.PY",
    "script.PY  ",
    ".py",
    "",
    "bot_telegram.py",
    "documento.pdf",
    "  SCRIPT.py "
]

archivos_limpios = []
for archivo in archivos_subidos:
    texto = archivo.lower().strip()
    if texto.endswith('py') and len(texto) > 3:
        archivos_limpios.append(texto)
    
archivos_sin_repetir = set(archivos_limpios)
print(f'Conjuntos sin repetidos {archivos_sin_repetir}')

archivos_lista = list(archivos_sin_repetir)
print(f'Elementos en la posicion 1: {archivos_lista[1]}')