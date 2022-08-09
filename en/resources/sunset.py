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

sense.clear(0, 0, 0)


def sunset():
    sense.set_pixels([a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([a, a, a, y, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([a, a, y, y, y, a, a, a,
                      a, a, a, y, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([a, a, a, y, a, a, a, a,
                      a, a, y, y, y, a, a, a,
                      a, a, a, y, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([a, a, a, a, a, a, a, a,
                      a, a, a, y, a, a, a, a,
                      a, a, y, y, y, a, a, a,
                      a, a, a, y, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, y, a, a, a, a,
                      a, a, y, y, y, a, a, a,
                      a, a, a, y, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, y, a, a, a, a,
                      a, a, y, y, y, a, a, a,
                      a, a, a, y, a, a, a, a,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, y, a, a, a, a,
                      r, r, y, y, y, r, r, r,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      r, r, r, r, r, r, r, r,
                      r, r, r, y, r, r, r, r,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      r, r, r, r, r, r, r, r,
                      r, r, r, r, r, r, r, r,
                      r, r, r, r, r, r, r, r,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([d, d, d, d, d, d, d, d,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      o, o, o, o, o, o, o, o,
                      r, r, r, r, r, r, r, r,
                      r, r, r, r, r, r, r, r,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([b, b, b, b, b, b, b, b,
                      d, d, d, d, d, d, d, d,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      o, o, o, o, o, o, o, o,
                      r, r, r, r, r, r, r, r,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([b, b, b, b, b, b, w, b,
                      b, b, b, b, b, b, b, b,
                      d, d, d, d, d, d, d, d,
                      a, a, a, a, a, a, a, a,
                      a, a, a, a, a, a, a, a,
                      o, o, o, o, o, o, o, o,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([b, b, w, b, b, b, b, b,
                      b, b, b, b, b, b, w, b,
                      b, b, b, b, b, b, b, b,
                      d, d, d, d, d, d, d, d,
                      a, a, a, a, a, a, a, a,
                      o, o, o, o, o, o, o, o,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([b, b, w, b, b, b, b, b,
                      b, b, b, b, b, b, w, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      d, d, d, d, d, d, d, d,
                      a, a, a, a, a, a, a, a,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([b, b, b, b, b, b, b, b,
                      b, b, w, b, b, b, b, b,
                      b, b, b, b, b, b, w, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      d, d, d, d, d, d, d, d,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
    sense.set_pixels([b, b, b, b, b, w, b, b,
                      b, b, b, b, b, b, b, b,
                      b, b, w, b, b, b, b, b,
                      b, b, b, b, b, b, w, b,
                      b, b, b, b, b, b, b, b,
                      b, b, b, b, b, b, b, b,
                      g, g, g, g, g, g, g, g,
                      g, g, g, g, g, g, g, g])
    sleep(1)
