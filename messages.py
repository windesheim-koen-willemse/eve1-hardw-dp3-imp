MESSAGE_CRITICAL = 'critical'
MESSAGE_WARNING = 'warning'
MESSAGE_INFO = 'info'

def send_event_message(kind, target, extras = {}):
    # final_dict = {'kind': kind, 'target': target} | extras
    print("[{}: {}] {}".format(kind, target, extras))