correos_sucios = [
    "  JUAN@GMAIL.COM  ",
    "pedro@hotmail.com",
    "   ",
    "juan@gmail.com",
    "maria@yahoo.es  ",
    "PEDRO@HOTMAIL.COM",
    "usuario_invalido",
    "",
    "  MARIA@yahoo.es "
]

correos_limpios = []
for correo in correos_sucios:
    texto = correo.strip().lower()
    if texto != '' and '@' in texto:
        correos_limpios.append(texto)

limpiando_repetidos = set(correos_limpios)
print(limpiando_repetidos)
