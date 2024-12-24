STATE_EMPTY = 0
STATE_CALM = 1
STATE_NORMAL = 2
STATE_BUSY = 3
STATE_FULL = 4

active_state = STATE_EMPTY

def transitions_to(possible_transitions):
    global active_state
    for target_state, condition in possible_transitions:
        if not condition: continue
        active_state = target_state
    pass

def handle_empty(is_trigger, people, time):
    transitions_to([
        (STATE_CALM, people > 0)
    ])

def handle_calm(is_trigger, people, time):
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
    transitions_to([
        (STATE_NORMAL, people < 130 and time <= 30), # Corrected
        (STATE_FULL, people == 160)
    ])

def handle_full(is_trigger, people, time):
    transitions_to([
        (STATE_BUSY, people < 160)
    ])