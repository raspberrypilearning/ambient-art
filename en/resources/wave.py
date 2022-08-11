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


def wave():
    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B])

    sleep(1)

    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, B, b, b, b, b, b,
                      b, B, B, b, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B])

    sleep(1)

    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, B, b, b, b, b,
                      b, b, B, B, b, b, b, b,
                      b, B, B, B, b, b, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B])

    sleep(1)

    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, B, b, b, b,
                      b, b, b, B, B, b, b, b,
                      b, b, B, B, b, b, b, b,
                      b, B, B, B, B, b, b, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B])

    sleep(1)

    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, B, w, b,
                      b, b, b, b, B, B, b, b,
                      b, b, b, B, B, B, b, b,
                      b, b, B, B, B, b, b, b,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B])

    sleep(1)

    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, w, b,
                      b, b, b, b, b, b, B, w,
                      b, b, b, b, b, B, B, w,
                      b, b, b, b, B, B, B, b,
                      B, b, b, B, B, b, b, b,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B])

    sleep(1)

    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, w,
                      b, b, b, b, b, b, B, w,
                      b, b, b, b, b, B, B, B,
                      B, B, b, b, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B])

    sleep(1)

    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, w, w,
                      b, b, b, b, b, b, B, B,
                      B, B, B, B, b, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B])

    sleep(1)

    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, w,
                      B, B, B, B, B, b, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B])

    sleep(1)

    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      B, B, B, B, B, B, w, w,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B])

    sleep(1)

    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B,
                      B, B, B, B, B, B, B, B])

    sleep(1)
