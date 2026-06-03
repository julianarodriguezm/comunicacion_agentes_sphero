import time
import random

from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color

CANAL = (4,)

toy = scanner.find_toy()

with SpheroEduAPI(toy) as sphero:

    objetivo_recibido = False

    # Verde = esperando
    sphero.set_main_led(Color(0, 255, 0))

    # Función que se ejecuta al recibir señal
    def recibir_senal(api, channel):

        global objetivo_recibido

        if channel != 4:
            return

        print("Señal recibida")

        objetivo_recibido = True

        # Amarillo = mensaje recibido
        api.set_main_led(Color(255, 255, 0))

    sphero.register_event(
        EventType.on_ir_message,
        recibir_senal
    )

    sphero.listen_for_ir_message(CANAL)

    while True:

        # Si NO ha recibido señal:
        if not objetivo_recibido:

            direccion = random.randint(0, 359)

            sphero.set_heading(direccion)
            sphero.set_speed(40)

            time.sleep(1)

        # Si recibió señal:
        else:

            # Se mueve "hacia objetivo"
            sphero.set_heading(0)

            sphero.set_speed(80)

            # Reenvía señal a otros robots
            sphero.send_ir_message(4, 1)

            print("Propagando señal")

            time.sleep(1)