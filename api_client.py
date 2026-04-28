import time

def check_virus_total(value, api_key=None):
    if not api_key:
        # Mock-данные (имитация работы API)
        return "Clean (Mock)" if len(value) % 2 == 0 else "Malicious (Mock)"
    
    # Здесь могла бы быть логика реального запроса к VirusTotal
    # Но для теста оставим имитацию
    return "Checked via API"