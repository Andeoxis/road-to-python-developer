promedio = 0
for i in range(1, 6):
    while True: 
        try:
            temperatura = int(input(f'Dame la temperatura N{i}:\n'))
            promedio = promedio + temperatura
            break
            
        except ValueError:
            print('ERROR: Solo puedes colocar numeros, intenta de nuevo.')

promedio = promedio / i
print(f'Promedio = {promedio}')
if promedio >= 45:
    print(f'ALERTA. El promedio de temperatura es critico. Activando ventiladores de emergencia.')
else:
    print(f'Temperatura del sistema estable.')