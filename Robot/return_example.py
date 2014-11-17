__author__ = 'hpiard'
__init__ = '__init__'

from time import sleep


def g(x):
    while True:
        y0 = x + 1
        y1 = x * 3
        y2 = y0 **3
        sleep(1)
        return y0, y1, y2


if __init__ == '__init__':
    while True:
        a = g(78)
        print a