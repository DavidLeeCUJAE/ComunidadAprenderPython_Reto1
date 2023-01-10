# Primer reto Nivel Facil de la Comunidad AprendePython (https://t.me/aprenderpython/30273/30286):
# Crea un programa que lea la hora de tu pc y que cuando ejecutes el programa, te salude dependiendo la hora, ej
# "Buen dia", "Buenas tardes" o "Buenas noches".
# Realizado por:
# ~Apuromafo (https://github.com/apuromafo/python_scripts/blob/main/script1.py)
# @DavidLeeCUJAE (https://github.com/DavidLeeCUJAE/Retos_ComunidadAprenderPython)

import time  # importar la librería time

# definir una función para obtener las horas
def get_time():
    t = time.localtime()
    horas = t[3]
    return horas


if __name__ == '__main__':
    hora_actual = get_time()
    # en dependencia de la hora cambio el saludo
    if hora_actual < 6 or hora_actual > 18:
        saludo = 'Buenas noches'
    elif hora_actual > 6 and hora_actual < 12:
        saludo = 'Buenos días'
    elif hora_actual > 12 and hora_actual < 18:
        saludo = 'Buenas tardes'
    # muestro el saludo
    print(f'{saludo}, la hora es {hora_actual}')
