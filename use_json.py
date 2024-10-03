import json, sys, os

def load_json(filename):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    creds_path = os.path.join(base_path, filename)

    with open(creds_path, 'r') as f:
        creds = json.load(f)
    return creds

creds = load_json('creds.json')