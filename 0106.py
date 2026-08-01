def bolivianos_a_dolares(monto_bs):
    conversion = monto_bs / 6.96
    return conversion


# 2. USAS LA FUNCIÓN (Pones a trabajar la máquina)
monto = 100
resultado_dolares = bolivianos_a_dolares(monto)

print(f"{monto} Bs equivalen a ${resultado_dolares:.2f} USD")