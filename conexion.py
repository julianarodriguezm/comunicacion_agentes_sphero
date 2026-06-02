from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
import time

toy = scanner.find_toy()

with SpheroEduAPI(toy) as sphero:
    sphero.set_main_led(Color(0, 255, 0))
    sphero.set_speed(50)

    time.sleep(2)

    sphero.set_speed(0)