# main.py
#
import argparse
import os
import logging
from scanner.scanner import scan_file_for_secrets

def scan_path(path):
    all_results = []

    if os.path.isfile(path):
        logging.info(f"Scanning file: {path}")
        all_results.extend(scan_file_for_secrets(path))
    elif os.path.isdir(path):
        logging.info(f"Scanning directory: {path}")
        for root, _, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                all_results.extend(scan_file_for_secrets(full_path))
    else:
        logging.error(f"Invalid path: {path}")
        return

    if all_results:
        print("\n Secrets Found:")
        for result in all_results:
            print(f"{result['filename']} [Line {result['line']}] ({result['type']}): {result['match']}")
    else:
        print("\n No secrets found.")

def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    parser = argparse.ArgumentParser(
        description="Scan files or directories for hardcoded secrets using regex patterns."
    )
    parser.add_argument('--path', required=True, help='Path to file or directory to scan')
    args = parser.parse_args()

    scan_path(args.path)

if __name__ == '__main__':
    main()

