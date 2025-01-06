from messages import send_event_message, MESSAGE_CRITICAL, MESSAGE_WARNING, MESSAGE_INFO
from tft import ICON_CALM, ICON_MID, ICON_BUSY

# CONSTANTS

STATE_EMPTY = 0
STATE_CALM = 1
STATE_NORMAL = 2
STATE_BUSY = 3
STATE_FULL = 4

# VARIABLES

active_state = STATE_EMPTY
cache_active_state = None

# UTILITIES

def transitions_to(possible_transitions):
    global active_state
    for target_state, condition in possible_transitions:
        if not condition: continue
        active_state = target_state
    pass

def active_state_to_text():
    if active_state == STATE_EMPTY: return "Empty"
    if active_state == STATE_CALM: return "Calm"
    if active_state == STATE_NORMAL: return "Normal"
    if active_state == STATE_BUSY: return "Busy"
    if active_state == STATE_FULL: return "Full"
    return "Unknown"

def active_state_to_icon():
    mapper = [
        (STATE_EMPTY, ICON_CALM),
        (STATE_CALM, ICON_CALM),
        (STATE_NORMAL, ICON_MID),
        (STATE_BUSY, ICON_BUSY),
        (STATE_FULL, ICON_BUSY)
    ]

    for match_to, icon in mapper:
        if active_state != match_to: continue
        return icon

# STATES

def handle_empty(is_trigger, people, time):
    if is_trigger: send_event_message(MESSAGE_CRITICAL, 'leeg')
    transitions_to([
        (STATE_CALM, people > 0)
    ])

def handle_calm(is_trigger, people, time):
    if is_trigger: send_event_message(MESSAGE_WARNING, 'rustig')
    transitions_to([
        (STATE_EMPTY, people == 0),
        (STATE_NORMAL, people > 30 and time > 5)
    ])

def handle_normal(is_trigger, people, time):
    transitions_to([
        (STATE_CALM, people <= 30 or time <= 5),
        (STATE_BUSY, people >= 130 or time > 30) # Corrected
    ])

def handle_busy(is_trigger, people, time):
    if is_trigger: send_event_message(MESSAGE_WARNING, 'druk')
    transitions_to([
        (STATE_NORMAL, people < 130 and time <= 30), # Corrected
        (STATE_FULL, people == 160)
    ])

def handle_full(is_trigger, people, time):
    if is_trigger: send_event_message(MESSAGE_CRITICAL, 'vol')
    transitions_to([
        (STATE_BUSY, people < 160)
    ])

handlers = [
    (STATE_EMPTY, handle_empty),
    (STATE_CALM, handle_calm),
    (STATE_NORMAL, handle_normal),
    (STATE_BUSY, handle_busy),
    (STATE_FULL, handle_full)
]

def handle_active_state(people, waiting_time):
    if waiting_time < 0: waiting_time = 10000000000000000000000000000000000
    global cache_active_state
    is_new_state = active_state != cache_active_state
    if is_new_state: cache_active_state = active_state

    for target_state, handler in handlers:
        if active_state != target_state: continue
        handler(is_new_state, people, waiting_time)