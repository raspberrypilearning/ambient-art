# m8tricks output file
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
a = (66, 220, 240)
y = (255, 255, 0)
g = (0, 255, 0)
r = (255, 0, 0)
b = (0, 0, 0)
d = (80, 80, 80)
w = (255, 255, 255)
o = (255, 150, 0)
B = (0, 0, 255)

sense.clear(0, 0, 0)


def tree():

    sense.set_pixels([B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      g, g, g, g, g, g, g, g])

    sleep(1)

    sense.set_pixels([B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      g, g, g, o, g, g, g, g])

    sleep(1)

    sense.set_pixels([B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, o, B, B, B, B,
                      g, g, g, o, g, g, g, g])

    sleep(1)

    sense.set_pixels([B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, o, B, B, B, B,
                      B, B, B, o, B, B, B, B,
                      g, g, g, o, g, g, g, g])

    sleep(1)

    sense.set_pixels([B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, g, g, g, B, B, B,
                      B, B, B, o, B, B, B, B,
                      B, B, B, o, B, B, B, B,
                      g, g, g, o, g, g, g, g])

    sleep(1)

    sense.set_pixels([B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, g, g, B, B, B,
                      B, B, g, g, g, B, B, B,
                      B, B, B, o, B, B, B, B,
                      B, B, B, o, B, B, B, B,
                      g, g, g, o, g, g, g, g])

    sleep(1)

    sense.set_pixels([B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, g, g, B, B, B, B,
                      B, B, g, g, g, g, B, B,
                      B, B, g, g, g, B, B, B,
                      B, B, B, o, B, B, B, B,
                      B, B, B, o, B, B, B, B,
                      g, g, g, o, g, g, g, g])

    sleep(1)

    sense.set_pixels([B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, g, g, g, B, B, B,
                      B, g, g, g, g, g, B, B,
                      B, B, g, g, g, B, B, B,
                      B, B, B, o, B, B, B, B,
                      B, B, B, o, B, B, B, B,
                      g, g, g, o, g, g, g, g])

    sleep(1)

    sense.set_pixels([B, B, B, B, B, B, B, B,
                      B, B, B, g, B, B, B, B,
                      B, B, g, g, g, g, B, B,
                      B, g, g, g, g, g, B, B,
                      B, B, g, g, g, B, B, B,
                      B, B, B, o, B, B, B, B,
                      B, B, B, o, B, B, B, B,
                      g, g, g, o, g, g, g, g])

    sleep(1)

    sense.set_pixels([B, B, B, B, B, B, B, B,
                      B, B, g, g, B, B, B, B,
                      B, g, g, g, g, g, B, B,
                      B, g, g, g, g, g, B, B,
                      B, B, g, g, g, B, B, B,
                      B, B, B, o, B, B, B, B,
                      B, B, B, o, B, B, B, B,
                      g, g, g, o, g, g, g, g])

    sleep(1)

    sense.set_pixels([B, B, B, g, B, B, B, B,
                      B, B, g, g, g, B, B, B,
                      B, g, g, g, g, g, B, B,
                      B, g, g, g, g, g, B, B,
                      B, B, g, g, g, B, B, B,
                      B, B, B, o, B, B, B, B,
                      B, B, B, o, B, B, B, B,
                      g, g, g, o, g, g, g, g])

    sleep(1)
