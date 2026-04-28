import re

# Регулярные выражения
IP_PATTERN = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
SHA256_PATTERN = r'\b[a-fA-F0-9]{64}\b'

def extract_data(file_path):
    found_data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            ips = re.findall(IP_PATTERN, content)
            hashes = re.findall(SHA256_PATTERN, content)
            
            for ip in set(ips):
                found_data.append({'value': ip, 'type': 'IP'})
            for h in set(hashes):
                found_data.append({'value': h, 'type': 'HASH'})
    except FileNotFoundError:
        return None
    return found_data