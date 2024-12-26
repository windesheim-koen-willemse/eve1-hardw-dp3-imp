from math import floor
from tft import tft_update
from states import active_state_to_icon

MINS_IN_HOUR = 60

def format_wachttijd(wachttijd_minuten):
    if wachttijd_minuten < 0: return "9+ uur"
    hours = floor(wachttijd_minuten / MINS_IN_HOUR)
    mins = floor(wachttijd_minuten % MINS_IN_HOUR)

    if hours < 1:
        return "{} min".format(mins)
    elif hours > 9:
        return "9+ uur"
    else:
        return "{} uur".format(hours)

def render(board, wachttijd):
    tft_update(board, active_state_to_icon(), format_wachttijd(wachttijd))