#  Hidden Scanner CLI

A Python-based command-line tool that scans files or directories for hardcoded secrets such as API keys, passwords, tokens, and private keys. Built for secure coding practice and regex-based detection.

##  Features
- Accepts both file and directory paths via CLI
- Uses regex to detect common secret patterns
- Outputs a clean report with filename, line number, match type, and matched string
- Includes logging for progress and errors

##  Detection Logic
The scanner uses regex patterns to detect:
- API Keys
- Passwords
- AWS Secret Access Keys
- Authorization Tokens
- Private Keys

##  Installation

Open this repository in GitHub Codespaces or clone locally.

```bash
pip install -r requirements.txt
