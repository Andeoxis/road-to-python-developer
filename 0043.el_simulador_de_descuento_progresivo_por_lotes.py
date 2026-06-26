# En tu distribuidora de pollos en Cochabamba, quieres premiar a los clientes mayoristas que te compran al por mayor.
# Vas a programar el sistema que calcula el precio de un pedido de 5 cajas de pollo, pero con una regla: mientras más cajas compra el cliente,
# más barata le sale la siguiente caja.

costo_de_caja_pollo = 0

for caja in range(1, 6):
    if caja <= 3:
        costo_de_caja_pollo += 150
        print(f'Caja N° {caja}: Precio normal (150)')
    else:
        costo_de_caja_pollo += 120
        print(f'Caja N° {caja}: Precio Oferta! (120)')
print(f'💰 Total a pagar por las {caja} cajas: {costo_de_caja_pollo} Bs, papuchin.')