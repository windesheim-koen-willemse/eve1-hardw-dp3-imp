from pyfirmata2 import Arduino
from util import get_register_pin
from states import handle_active_state
from model import log_model_values, record_people_change, CHANGE_ENTER, CHANGE_LEAVE, get_people_in_queue, get_waiting_time_in_queue, update_screen
from time import time
from ui import render
from testability import symclick

# CONSTANTS

SAMPLING_RATE = 10
MODEL_CALC_INTERVAL = 3

# VARIABLES

timer_end = time()+MODEL_CALC_INTERVAL

# SETUP

board = Arduino(Arduino.AUTODETECT)
board.samplingOn(SAMPLING_RATE)

enter_queue_output_pin = board.get_pin('d:4:o')
def on_enter_queue(is_btn_on):
    enter_queue_output_pin.write(is_btn_on)
    if not is_btn_on: return
    record_people_change(CHANGE_ENTER)
get_register_pin(board, 'd:2:i', on_enter_queue)

leave_queue_output_pin = board.get_pin('d:5:o')
def on_leave_queue(is_btn_on):
    leave_queue_output_pin.write(is_btn_on)
    if not is_btn_on: return
    record_people_change(CHANGE_LEAVE)
get_register_pin(board, 'd:3:i', on_leave_queue)

render(board, 0)

# LOOP

while True:
    current_time = time()
    if current_time > timer_end:
        log_model_values()

    handle_active_state(get_people_in_queue(), get_waiting_time_in_queue())

    if current_time > timer_end:
        update_screen(board)
        timer_end = current_time + MODEL_CALC_INTERVAL