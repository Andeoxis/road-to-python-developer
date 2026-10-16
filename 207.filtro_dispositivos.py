dispositivos_crudos = [
    "  ESP32_PORT_1  ",
    "ARDUINO_UNO",
    "   ",
    "esp32_port_1",
    "SENSOR_DHT22  ",
    "ESP32_",
    "",
    "esp32_port_2",
    "MODEM_GSM",
    "  ESP32_PORT_2 "
]

dispositivos_limpios = []
for dispositivos in dispositivos_crudos:
    texto = dispositivos.strip().lower()
    if texto.startswith('esp32_') and len(texto) > 6:
        dispositivos_limpios.append(texto)

dispositivos_sin_repetir = set(dispositivos_limpios)
dispositivos_lista = list(dispositivos_sin_repetir)
print(dispositivos_lista)
print(dispositivos_lista[1])