ERR = True
OK = False

def get_register_pin(board, pin, callback):
    pin = board.get_pin(pin)
    pin.register_callback(callback)
    pin.enable_reporting()
    return pin