import unittest
import io
import runpy
from unittest.mock import patch

class TestZad10(unittest.TestCase):

    def run_script(self, inputs):
        """Uruchamia skrypt liczący wystąpienia litery."""
        with patch('builtins.input', side_effect=inputs):
            captured_output = io.StringIO()
            with patch('sys.stdout', captured_output):
                runpy.run_path('zad10.py', run_name='__main__')
            return captured_output.getvalue().strip()

    def test_char_exists(self):
        """Testuje, gdy litera występuje w tekście."""
        output = self.run_script(['hello world', 'l'])
        self.assertEqual(output, "Litera 'l' występuje w tekście 3 razy.")

    def test_char_not_exists(self):
        """Testuje, gdy litera nie występuje w tekście."""
        output = self.run_script(['hello world', 'z'])
        self.assertEqual(output, "Litera 'z' występuje w tekście 0 razy.")

    def test_case_sensitive(self):
        """Testuje rozróżnianie wielkości liter."""
        output = self.run_script(['Hello World', 'h'])
        self.assertEqual(output, "Litera 'h' występuje w tekście 0 razy.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
