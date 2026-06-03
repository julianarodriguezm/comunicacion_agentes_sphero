import time
import random

from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

CANAL = 4

toy = scanner.find_toy()

with SpheroEduAPI(toy) as sphero:

    # Azul = explorando
    sphero.set_main_led(Color(0, 0, 255))

    # Movimiento aleatorio inicial
    for _ in range(10):

        direccion = random.randint(0, 359)

        sphero.set_heading(direccion)
        sphero.set_speed(60)

        time.sleep(1.5)

    # Simulación de "objetivo encontrado"
    print("Objetivo encontrado")

    # Rojo = encontró objetivo
    sphero.set_main_led(Color(255, 0, 0))

    # Detenerse
    sphero.set_speed(0)

    # Enviar señal IR a otros robots
    while True:
        sphero.send_ir_message(CANAL, 1)

        print("Enviando señal")

        time.sleep(1)