from tft import tft_update
from states import active_state_to_icon

def render(board):
    tft_update(board, active_state_to_icon(), "Hi")