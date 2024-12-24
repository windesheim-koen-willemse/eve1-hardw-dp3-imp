from pyfirmata2 import Arduino
from util import get_register_pin
from states import handle_active_state

# VARIABLES

people = 0

# SETUP

board = Arduino(Arduino.AUTODETECT)
board.samplingOn(10)

def on_inc(on):
    if not on: return
    people += 1
inc_pin = get_register_pin(board, 'd:2:i', on_inc)

def on_dec(on):
    if not on: return
    people -= 1
dec_pin = get_register_pin(board, 'd:3:i', on_dec)

# Main
while True:
    handle_active_state(people)