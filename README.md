# Hidden Scanner CLI

A lightweight command-line tool to detect hardcoded secrets in text files and directories using regex-based pattern matching.

---

##  Features

-  Scans individual files or entire directories
-  Detects secrets using 5 regex patterns:
  - API Keys
  - Passwords
  - AWS Secret Access Keys
  - Authorization Tokens
  - Private Keys
-  Outputs filename, line number, match type, and matched string
-  Logs scanning progress and errors using Python's `logging` module
-  Simple CLI interface powered by `argparse`

---

##  Tests Run
python main.py --path ./Line.txt
python main.py --path ./Newfolder
python main.py --path ./secrets_test.txt
python main.py --path ./rubric3_test.txt
python main.py --path ./rubric4_folder

A screen print of the successful runs has been uploaded as Screenprint.docx

A 1 minute video recordinf could not be saved for data restrictions - Please use Microsoft Word Reader to play the audio part of the computer video  for RecordingtobepalyedewithMicrosoftReader,

