# Pida al usuario que ingrese el monto total de su compra (un número con decimales).

# Si el monto es menor a 0, el programa debe mostrar un mensaje de error diciendo que el monto no es válido.

# Aplique las siguientes reglas de descuento:

# Si la compra es menor a 100 bs, no tiene descuento (0%).

# Si la compra está entre 100 bs y 500 bs (inclusive ambos), se aplica un 10% de descuento.

# Si la compra es mayor a 500 bs, se aplica un 20% de descuento.

# Calcule el monto del descuento y el total final a pagar (monto original menos el descuento).

# Muestre los resultados en la pantalla dejando una línea en blanco después de las preguntas (como aprendiste en el anterior ejercicio), dibujando una línea de guiones, y mostrando:

# El descuento aplicado en bs.

# El total neto a pagar.
while True:
    monto_total_de_cuenta = float(input('Ingrese el monto total de su compra: '))


    if monto_total_de_cuenta <= 0:
        print('El monto ingresado no es valido')
        print('Porfavor vuelva a intentarlo')
        
    elif monto_total_de_cuenta < 100:
      descuento = 0
      descuento_en_bolivianos = 0
      total_menos_el_descuento = monto_total_de_cuenta
      print('No tiene descuento')
      break
    elif monto_total_de_cuenta >= 100 and monto_total_de_cuenta <= 500:
        descuento = 10
        division_entre_cien = 100
        factor_decimal = descuento / division_entre_cien
        descuento_en_bolivianos = monto_total_de_cuenta * factor_decimal
        total_menos_el_descuento = monto_total_de_cuenta - descuento_en_bolivianos
        break
    
    elif monto_total_de_cuenta > 500:
        descuento = 20
        division_entre_cien = 100
        factor_decimal = descuento / division_entre_cien
        descuento_en_bolivianos = monto_total_de_cuenta * factor_decimal
        total_menos_el_descuento = monto_total_de_cuenta - descuento_en_bolivianos
        break

print(f'\nEl descuento es del {descuento}%')
print(f'El descuento en bs es del {descuento_en_bolivianos}')
print(f'El total sin descuento es del {monto_total_de_cuenta}')
print(f'El total menos el descuento es del {total_menos_el_descuento} ')
