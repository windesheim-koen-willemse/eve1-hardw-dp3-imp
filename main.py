from pyfirmata2 import Arduino
from tft import tft_update
from util import get_register_pin, STATUS_CALM, STATUS_MID, STATUS_BUSY

# Globals
statuses = [STATUS_CALM, STATUS_MID, STATUS_BUSY]
num = 0

# Caches
cache_num = None

# Config
board = Arduino(Arduino.AUTODETECT)
board.samplingOn(10)

def on_inc(on):
    global num
    if not on: return
    num += 1
inc_pin = get_register_pin(board, 'd:2:i', on_inc)

def on_dec(on):
    global num
    if not on: return
    num -= 1
dec_pin = get_register_pin(board, 'd:3:i', on_dec)

# Main
while True:
    if cache_num == num: continue
    cache_num = num
    tft_update(board, statuses[num%len(statuses)], "{} per.".format(num))