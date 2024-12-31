from time import time

symclick_t = None

def symclick(interval, clicker_function):
    global symclick_t
    if symclick_t == None:
        symclick_t = time() + interval
        clicker_function(True)
    if time() > symclick_t:
        print("[symclick]")
        clicker_function(True)
        symclick_t = time() + interval