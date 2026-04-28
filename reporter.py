import csv
import json
from datetime import datetime

def save_report(data, output_path, format):
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for item in data:
        item['date'] = date_now

    if format == 'csv':
        keys = data[0].keys()
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
            
    elif format == 'json':
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)