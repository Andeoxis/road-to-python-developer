def obtener_permisos(letra):
    match dato:
        case 'admin':
            return 'Acceso total al sistema.'
        case 'editor':
            return 'Puede crear y modificar el contenido.'
        case 'visitante':
            return 'Solo lectura.'
        case _:
            return 'ERROR. Dato erroneo.'

dato = input('Ingrese alguna de las opciones (admin/editor/visitante):\n').lower().strip()
respuesta =obtener_permisos(dato)
print(f'Tu tienes permiso de: {respuesta}')