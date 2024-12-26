from time import time
from messages import send_event_message, MESSAGE_INFO
from ui import render

# CONSTANTS

MAX_HISTORY_LENGTH = 255

CHANGE_ENTER = 0
CHANGE_LEAVE = 1

# VARIABLES

people_in_queue = 0
waiting_time_in_queue = 0

change_history = []

#  UTILS

def cap_history_at(max):
    while len(change_history) > max:
        del change_history[0]

def record_people_change(kind):
    global people_in_queue
    people_in_queue += 1 if kind == CHANGE_ENTER else -1
    
    current_time = time()
    change_history.append((kind, current_time))
    cap_history_at(MAX_HISTORY_LENGTH)

def seconds_to_minutes(seconds):
    return seconds/60

#  MODEL

def history_to_growth_factor(kind):
    change_history.sort(key=lambda v: v[1])
    recording_start = change_history[0][1]
    recorded_time = max(time() - recording_start, 1)
    amount_of_matches = len(list(filter(lambda v: v[0] == kind, change_history)))
    return amount_of_matches / seconds_to_minutes(recorded_time)

def calc_model_values():
    if len(change_history) == 0: return (0, 0, 0, 0)
    I = history_to_growth_factor(CHANGE_ENTER)
    M = history_to_growth_factor(CHANGE_LEAVE)
    N = I / (M-I) if M != I and M-I != 0 else 0
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