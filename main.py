from pyfirmata2 import Arduino
from util import get_register_pin

board = Arduino(Arduino.AUTODETECT)
board.samplingOn(10)

def on_inc(on):
    if not on: return
    pass
inc_pin = get_register_pin(board, 'd:2:i', on_inc)

def on_dec(on):
    if not on: return
    pass
dec_pin = get_register_pin(board, 'd:3:i', on_dec)

# Main
while True:
    pass