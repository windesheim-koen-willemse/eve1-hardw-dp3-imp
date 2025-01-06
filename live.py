from time import time

TEMPLATE_FILE = "./live-data.html"
TEMPLATE_MARK = "<!---->"

def get_current_code():
    return open(TEMPLATE_FILE, 'r').read()

def where_to_insert_new_data(current_code: str):
    for i in range(len(current_code)):
        if not current_code[i:].startswith(TEMPLATE_MARK): continue
        return i + len(TEMPLATE_MARK)
    return 0

def save_new_code(new_code):
    open(TEMPLATE_FILE, 'w').write(new_code)

def update_live_data(status, wachttijd, verwachtte_wachtrij, wachtrij, aankomst_snelheid, tijd=None):
    if tijd == None: tijd = time()
    current_code = get_current_code()
    code_to_insert = f"<tr><td>{status}</td><td>{wachttijd}</td><td>{verwachtte_wachtrij}</td><td>{wachtrij}</td><td>{aankomst_snelheid}</td><td>{tijd}</td></tr>"
    insert_location = where_to_insert_new_data(current_code)
    new_code = current_code[:insert_location] + code_to_insert + current_code[insert_location:]
    save_new_code(new_code)