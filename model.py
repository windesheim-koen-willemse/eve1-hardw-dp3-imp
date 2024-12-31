from time import time
from messages import send_event_message, MESSAGE_INFO
from ui import render

# CONSTANTS

MAX_RECORD_LIVING_TIME_IN_SEC = 3600 # 1 hour
M = 10.5

CHANGE_ENTER = 0
CHANGE_LEAVE = 1

# VARIABLES

people_in_queue = 100
waiting_time_in_queue = 0

new_people_histo = []

#  UTILS

def remove_old_enter_records(time_before_now):
    min_time = time() - time_before_now
    for record_index in range(len(new_people_histo)-1, -1, -1):
        if new_people_histo[record_index] >= min_time: continue
        del new_people_histo[record_people_change]

def record_people_change(kind, record_time = time()):
    global people_in_queue
    people_in_queue += 1 if kind == CHANGE_ENTER else -1

    if kind == CHANGE_LEAVE: return people_in_queue
    
    new_people_histo.append(record_time)
    remove_old_enter_records(MAX_RECORD_LIVING_TIME_IN_SEC)
    return people_in_queue

def seconds_to_minutes(seconds):
    return seconds/60

#  MODEL

def history_to_growth_factor():
    new_people_histo.sort()
    recording_start = new_people_histo[0]
    recorded_time = max(time() - recording_start, 1)
    return len(new_people_histo) / seconds_to_minutes(recorded_time)

def calc_model_values():
    if len(new_people_histo) == 0: return (0, 0, 0, 0)
    I = history_to_growth_factor()
    N = I / (M-I) if M-I != 0 else 0
    T = N / I if I != 0 else 0
    S = 1 / M if M != 0 else 0
    W = T - S
    return (N, W, I, M)

def log_model_values(board):
    global waiting_time_in_queue

    N, W, I, M = calc_model_values()

    waiting_time_in_queue = W
    render(board, W)
    send_event_message(MESSAGE_INFO, 'timer', {
        'wachtrij': N,
        'wachttijd': W,
        'V_aankomst': I,
        'V_vertrek': M
    })