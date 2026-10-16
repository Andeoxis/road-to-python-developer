alertas = [
    "temperatura_alta",
    "voltaje_bajo",
    "temperatura_alta",
    "conexion_perdida",
    "temperatura_alta",
    "voltaje_bajo",
    "memoria_llena"
]
temperaturas = {}
for num_tempe in alertas:
    acumulado = temperaturas.get(num_tempe, 0)
    temperaturas[num_tempe] = acumulado + 1
print(temperaturas)

for estado, veces in temperaturas.items():
    if veces >= 3:
        print(f'Estado Critico: {estado} ocurrio {veces} veces')
    else:
        print(f'Estado normal: {estado} ocurrio {veces} veces')