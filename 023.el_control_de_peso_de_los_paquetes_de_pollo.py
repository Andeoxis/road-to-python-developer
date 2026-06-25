# Vámonos a tu terreno, el negocio de los pollos.
# Imagina que estás programando la balanza digital para empaquetar pollos al por mayor.
# Por estándar de calidad, cada bolsa empaquetada debe pesar entre 10 y 15 kilos.

# Si el operador pone una bolsa que pesa menos de 10 kilos (muy flaco) O si pesa más de 15 kilos (muy pesado),
# la balanza debe rechazar el paquete y exigir que se acomode el peso.

bolsa_empaquetada = int(input('Cuanto pesa el paquete de pollo (debe estar en el rango de 10 y 15 kilos)'))
while bolsa_empaquetada < 10 or bolsa_empaquetada > 15:
    print('Peso fuera del rango, intente de nuevo')
    bolsa_empaquetada = int(input('Cuanto pesa el paquete de pollo (debe estar en el rango de 10 y 15 kilos)'))
print('El peso es bueno, esta listo para la venta')