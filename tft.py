from pyfirmata2 import util, STRING_DATA
from util import ERR, OK

_MAX_SHOWN_TIME_CHARACTERS = 7
_SERIAL_FORMAT = "{status}{txt}"

def send_serial_string(board, txt):
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(txt))

def tft_update(board, business_status, time_str):
    if len(time_str) >= _MAX_SHOWN_TIME_CHARACTERS:
        return ERR
    else:
        formatted_msg = _SERIAL_FORMAT.format(status=business_status, txt=time_str)
        send_serial_string(board, formatted_msg)
        return OK