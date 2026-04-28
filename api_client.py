import time

def check_virus_total(value, api_key=None):
    if not api_key:
       
        return "Clean (Mock)" if len(value) % 2 == 0 else "Malicious (Mock)"
    return "Checked via API"
