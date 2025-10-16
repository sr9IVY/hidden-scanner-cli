# scanner/scanner.py

import re

# Example regex patterns — you can expand this list
SECRET_PATTERNS = [
    r'api[_-]?key\s*=\s*[\'"][A-Za-z0-9_\-]{16,}[\'"]',
    r'password\s*=\s*[\'"].+[\'"]',
    r'aws[_-]?secret[_-]?access[_-]?key\s*=\s*[\'"].+[\'"]',
    r'authorization\s*=\s*[\'"].+[\'"]',
    r'private[_-]?key\s*=\s*[\'"].+[\'"]'
]

def scan_file_for_secrets(file_path):
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, start=1):
                for pattern in SECRET_PATTERNS:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        results.append({
                            'filename': file_path,
                            'line': line_num,
                            'match': match.group()
                        })
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return results
