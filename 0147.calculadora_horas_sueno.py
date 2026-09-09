def evaluar_descanso(hora_dormir, hora_despertar):
    """Calculadora y evaluador de tiempo de sueno nocturno"""
    if hora_despertar >= hora_dormir:
        horas = hora_despertar - hora_dormir
    else:
        horas = (24 - hora_dormir) + hora_despertar

    if horas < 7:
        diagnostico = "Insuficiente"
    elif horas <= 9:
        diagnostico = "Optimo"
    else:
        diagnostico = "Excesivo"

    return horas, diagnostico


print(f"\n{evaluar_descanso.__doc__}")

while True:
    try:
        dormir = int(input("Hora a la que se durmio (0-23): "))
        if dormir < 0 or dormir > 23:
            raise ValueError

        despertar = int(input("Hora a la que desperto (0-23): "))
        if despertar < 0 or despertar > 23:
            raise ValueError

        if dormir == despertar:
            raise ValueError

        break
    except ValueError:
        print("ERROR: Ingrese horas validas en formato 24h y distintas entre si.\n")

horas_dormidas, calidad = evaluar_descanso(dormir, despertar)
print("\nResultado del descanso:")
print(f"Horas totales de sueno: {horas_dormidas} h - Diagnostico: {calidad}")