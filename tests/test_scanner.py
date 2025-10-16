# tests/test_scanner.py

import unittest
from scanner.scanner import scan_file_for_secrets
import tempfile
import os

class TestSecretScanner(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        self.test_file.write("api_key = '12345-ABCDE'\n")
        self.test_file.write("password = 'hunter2'\n")
        self.test_file.write("normal_line = 'hello world'\n")
        self.test_file.close()

    def test_secret_detection(self):
        results = scan_file_for_secrets(self.test_file.name)
        self.assertTrue(any("api_key" in r['match'] for r in results))
        self.assertTrue(any("password" in r['match'] for r in results))
        self.assertFalse(any("hello world" in r['match'] for r in results))

    def tearDown(self):
        os.unlink(self.test_file.name)

if __name__ == '__main__':
    unittest.main()
