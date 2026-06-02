import time
import random
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color

# Canal de comunicación IR entre robots
CANAL_OBJETIVO = (4,)

# Busca un Sphero cercano por Bluetooth
toy = scanner.find_toy()

with SpheroEduAPI(toy) as sphero:

    # Estado inicial: robot normal, no ha recibido señal
    objetivo_detectado = False

    # Función que se ejecuta cuando recibe señal IR
    def recibir_senal(api, channel):
        global objetivo_detectado

        if channel != 4:
            return

        print("Señal recibida: objetivo encontrado")

        api.set_main_led(Color(255, 0, 0))  # rojo = informado
        api.set_speed(0)

        # Aquí luego se puede agregar lógica para ir hacia la zona objetivo
        time.sleep(1)

        # Sigue escuchando señales
        api.listen_for_ir_message(CANAL_OBJETIVO)

    # Registrar evento de recepción IR
    sphero.register_event(EventType.on_ir_message, recibir_senal)
    sphero.listen_for_ir_message(CANAL_OBJETIVO)

    # LED inicial: azul = explorando
    sphero.set_main_led(Color(0, 0, 255))

    # Movimiento aleatorio básico
    while True:
        direccion = random.randint(0, 359)  # ángulo de movimiento
        velocidad = random.randint(40, 80)  # velocidad moderada

        sphero.set_heading(direccion)
        sphero.set_speed(velocidad)

        time.sleep(2)

        sphero.set_speed(0)
        time.sleep(0.5)