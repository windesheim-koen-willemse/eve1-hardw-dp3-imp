ERR = True
OK = False

STATUS_CALM = 0
STATUS_MID = 1
STATUS_BUSY = 2

def get_register_pin(board, pin, callback):
    pin = board.get_pin(pin)
    pin.register_callback(callback)
    pin.enable_reporting()
    return pin