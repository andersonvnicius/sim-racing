from pyfirmata import Arduino, util
import time

board = Arduino('COM12')

iterator = util.Iterator(board)
iterator.start()

n_of_leds = 8
n_of_pots = 2

D_pins = []
A_pins = []

for i in range(0, n_of_leds):
    D_pins.append(board.get_pin('d:'+str(i+2)+':o'))
    D_pins[i].write(1)

for i in range(0, n_of_pots):
    A_pins.append(board.get_pin('a:'+str(i)+':i'))

"""
while True:
    for i in range(0,n_of_leds):
        D_pins[i].write(1)
        time.sleep(0.05)
        D_pins[i].write(0)

    for i in reversed(range(0, n_of_leds)):
        D_pins[i].write(1)
        time.sleep(0.05)
        D_pins[i].write(0)
"""