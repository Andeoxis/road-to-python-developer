entradas_stock = [
    ("resistencia", 50),
    ("led_rojo", 20),
    ("resistencia", 30),
    ("pulsador", 10),
    ("led_rojo", 15),
    ("esp32", 2),
    ("resistencia", 20),
    ("esp32", 3)
]

stock_total = {}

for componente, cantidad in entradas_stock:
    acumulado_anterior = stock_total.get(componente, 0)
    stock_total[componente] = acumulado_anterior + cantidad
print(stock_total)