import unittest
import io
import runpy
from unittest.mock import patch

class TestZad12(unittest.TestCase):

    def run_script(self, word_input):
        """Uruchamia skrypt sprawdzający palindromy."""
        with patch('builtins.input', return_value=word_input):
            captured_output = io.StringIO()
            with patch('sys.stdout', captured_output):
                runpy.run_path('zad12.py', run_name='__main__')
            return captured_output.getvalue().strip()

    def test_is_palindrome(self):
        """Testuje dla słowa, które jest palindromem."""
        output = self.run_script('kajak')
        self.assertEqual(output, "Słowo 'kajak' jest palindromem.")

    def test_is_not_palindrome(self):
        """Testuje dla słowa, które nie jest palindromem."""
        output = self.run_script('python')
        self.assertEqual(output, "Słowo 'python' nie jest palindromem.")

    def test_is_palindrome_case_insensitive(self):
        """Testuje palindrom z różną wielkością liter."""
        output = self.run_script('Kajak')
        self.assertEqual(output, "Słowo 'Kajak' jest palindromem.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
