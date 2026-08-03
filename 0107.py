def crea_correo(nombre, apellido):
    creando_correo = nombre + '.' + apellido + '@empresa.com'
    return creando_correo

resultado = crea_correo('Anthony', 'vasquez')
print(f'Tu correo es: {resultado}')