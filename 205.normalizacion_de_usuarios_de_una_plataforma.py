usuarios_crudos = [
    "  @alex_99  ",
    "admin",
    "   ",
    " @ALEX_99",
    "carlos_dev  ",
    "@sofia.tech",
    "",
    "@carlos_dev",
    "invitado_anonimo",
    "  @SOFIA.TECH ",
    "  sof@ct_98"
]

usuarios_limpios = []
for usuario in usuarios_crudos:
    texto = usuario.lower().strip()
    if texto.startswith('@'):
        usuarios_limpios.append(texto)

limpiado_repetidos = set(usuarios_limpios)
print(limpiado_repetidos)