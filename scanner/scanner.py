# scanner/scanner.py

import re
import logging

# Define regex patterns for secret detection
SECRET_PATTERNS = {
    "API Key": r'api[_-]?key\s*=\s*[\'"][A-Za-z0-9_\-]{16,}[\'"]',
    "Password": r'password\s*=\s*[\'"].+[\'"]',
    "AWS Secret Access Key": r'aws[_-]?secret[_-]?access[_-]?key\s*=\s*[\'"].+[\'"]',
    "Authorization Token": r'authorization\s*=\s*[\'"].+[\'"]',
    "Private Key": r'private[_-]?key\s*=\s*[\'"].+[\'"]'
}

def scan_file_for_secrets(file_path):
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, start=1):
                for label, pattern in SECRET_PATTERNS.items():
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        results.append({
                            'filename': file_path,
                            'line': line_num,
                            'type': label,
                            'match': match.group().strip()
                        })
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
    return results

