# Ejercicio: Calculadora de propinas y división de cuenta
# Enunciado:
# Imagina que fuiste a comer con tus amigos y quieren dividir la cuenta de forma equitativa, incluyendo una propina para el mesero. Debes escribir un programa en Python que haga lo siguiente:

# Pida al usuario el total de la cuenta (puede tener decimales).

# Pida el porcentaje de propina que quieren dejar (por ejemplo: 10, 15 o 20).

# Pida el número de personas entre las que se va a dividir la cuenta.

# Calcule el total de la propina, el total general (cuenta + propina) y cuánto debe pagar cada persona.

# Muestre los resultados en la pantalla con un mensaje claro.

cuenta_total = float(input('Ingrese el total a pagar de la cuenta: '))
porcentaje_propina = int(input('Ingrese el porcentaje de propina que quisiera dejar: '))
# Corrección aquí:
numero_de_personas = int(input('Ingrese el numero de personas para dividir la cuenta: '))
print()

total_de_propina = (cuenta_total * porcentaje_propina) / 100
total_general = total_de_propina + cuenta_total
Cuanto_debe_pagar_cada_uno = total_general / numero_de_personas

print(50 * '-', '\n') 
print(f'Total de propina es {total_de_propina}bs')
print(f'Total general es {total_general}bs')
print(f'Cada uno debe pagar {Cuanto_debe_pagar_cada_uno}bs \n')
print(50 * '-')
print()