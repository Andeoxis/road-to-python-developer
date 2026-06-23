'''
Docstring for terminos_mas_utilizados_en_programacion
'''
significados = {
    'python': 'Un lenguaje de programación muy usado',
    'visual studio': 'Un entorno de desarrollo de Microsoft',
    'variable': 'Un espacio donde se guarda información',
    'algoritmo': 'Conjunto de pasos para llegar a una solución o resolver una tarea',
    'analisis de complejidad': '''
    Evaluación de la eficiencia de un algoritmo en términos de tiempo de ejecución y espacio en memoria en función del tamaño de la entrada
    ''',
    'api': 'Una API permite que una aplicación acceda a las funcionalidades o datos de otra',
    'api graphql': '''
    Es una interfaz o herramienta que te permite pedir exactamente lo que necesitas sin darte datos innecesarios
    ''',
    'api key': '''
    Clave de autenticación utilizada para acceder a una API. Es una forma segura de controlar el acceso a los recursos y gestionar las credenciales.
    ''',
    'api restful': 'Es una interfaz sencilla y comun que todos los programas utilizan para hablar entre ellos',
    'argumento': 'El argumento es la información que le pasas a una variable ',
    'array': 'El array es una lista para guardar, remplazar y mostrar datos',
    'atributo': 'Es un detalle, una pequeña información para describir un objeto '
}
consulta = input('¿Qué palabra quieres buscar?: ').lower()
if consulta in significados:
    print(f'Significado de "{consulta}": {significados[consulta]}')
else:
    print('Esa palabra no está registrada.')
