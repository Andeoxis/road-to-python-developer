mascotas = []

for i in range(1, 6):
    while True:
        try:
            nombre_mascotas = input(f'Ingresa el nombre de la mascota N{i}:\n').lower().strip()
            if nombre_mascotas == '' or nombre_mascotas.isdigit() or len(nombre_mascotas) > 12:
                raise ValueError
            mascotas.append(nombre_mascotas)
            break
        except ValueError:
            print('ERROR: Te equivocaste en algun dato, intenta de nuevo.')
        
perros_diferentes_nombre = list(set(mascotas))
numero_de_perros_diferentes = len(perros_diferentes_nombre)
perro_especial = 'fido' in perros_diferentes_nombre
nombres_cortos = 0
for m in mascotas:
    if len(m) <= 5:
        nombres_cortos += 1
print('----- REGISTRO DE MASCOTAS EN EL VETERINARIO -----')
print(f'Esta es la lista de nombres de todas las mascotas: {mascotas}')
print(f'Esta es la lista sin repetir nombres: {perros_diferentes_nombre}')
print(f'Este es el numero de perros sin repetir nombre: {numero_de_perros_diferentes}')
print(f'Estas son las mascotas con nombre corto: {nombres_cortos}')

if perro_especial:
    print('Esta Fido el perro especial, Felicidades.')
else:
    print('El perrito fido al parecer no vino.')

