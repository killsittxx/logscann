import argparse
from utils import setup_logging
from scanner import extract_data
from api_client import check_virus_total
from reporter import save_report

logger = setup_logging()

def main(): 
    parser = argparse.ArgumentParser(description="LogScan CLI Tool")
    parser.add_argument("-log-file", required=True, help="Path to log file")
    parser.add_argument("-api-key", help="VirusTotal API Key (optional)")
    parser.add_argument("-output", required=True, help="Output report path")
    parser.add_argument("-format", choices=['csv', 'json'], required=True, help="Report format")
    
    args = parser.parse_args()
    logger.info(f"Started scanning file: {args.log_file}")
    data = extract_data(args.log_file)
    if data is None:
        logger.error(f"File not found: {args.log_file}")
        print("Error: Log file not found.")
        return
    print("--- LogScan script started ---")
    # 2. Проверка через API
    print(f"Found {len(data)} items. Checking...")
    for item in data:
        item['result'] = check_virus_total(item['value'], args.api_key)
        logger.info(f"Checked {item['type']}: {item['value']} -> {item['result']}")

    # 3. Сохранение
    save_report(data, args.output, args.format)
    print(f"Report saved to {args.output}")
    logger.info("Scan completed successfully.")

if __name__ == "__main__":
    main()
