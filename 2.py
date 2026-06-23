# a = 9
# b = 2
# c = 11
# d = 9 % 2
# e = 2 % 3
# f = 11 % 10
# print(f'a = {a}')
# print(f'b = {b}')
# print(f'c = {c}')
# print(f'd = {d}')
# print(f'e = {e}')
# print(f'f = {f}')


# Desafío

# Principiante
# Estás ayudando a una tienda de mascotas a crear un sistema para determinar si pueden vender una mascota a un cliente.

# Inicializa las siguientes variables:

# has_license con el valor True
# has_space con el valor True
# has_experience con el valor False
# Escribe expresiones lógicas para determinar si:

# can_sell_regular_pet: El cliente puede comprar una mascota regular si tiene YA SEA una licencia O experiencia, Y debe tener espacio
# can_sell_exotic_pet: El cliente puede comprar una mascota exótica si tiene AMBAS una licencia Y experiencia, Y debe tener espacio
# cannot_sell_any_pet: La tienda NO PUEDE vender ninguna mascota si el cliente NO tiene licencia Y NO tiene experiencia, O NO tiene espacio
# Resultados esperados con los valores dados:

# can_sell_regular_pet: True (tiene licencia y espacio)
# can_sell_exotic_pet: False (no tiene experiencia)
# cannot_sell_any_pet: False (tiene licencia y espacio)

# Hints icon
# Pistas

# Pista 1
# Revelado
# Toggle hint
# Pista 2
# Toggle hint
# Pista 3
# Toggle hint

# Solución

# Solución
# Revelado

# # Initialize variables
# has_license = True
# has_space = True
# has_experience = False

# # Calculate conditions
# can_sell_regular_pet = (has_license or has_experience) and has_space
# can_sell_exotic_pet = has_license and has_experience and has_space
# cannot_sell_any_pet = (not has_license and not has_experience) or not has_space

# # Print results
# print("Can sell regular pet:", can_sell_regular_pet)
# print("Can sell exotic pet:", can_sell_exotic_pet)
# print("Cannot sell any pet:", cannot_sell_any_pet)
