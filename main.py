from pyfirmata2 import Arduino
from util import STATUS_MID
from tft import tft_update

board = Arduino(Arduino.AUTODETECT)

tft_update(board, STATUS_MID, "7m")

while True:
    pass