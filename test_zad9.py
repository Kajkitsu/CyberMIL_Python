import unittest
import io
import runpy
from unittest.mock import patch

class TestZad9(unittest.TestCase):

    def run_script(self, text_input):
        """Uruchamia skrypt odwracający string."""
        with patch('builtins.input', return_value=text_input):
            captured_output = io.StringIO()
            with patch('sys.stdout', captured_output):
                runpy.run_path('zad9.py', run_name='__main__')
            return captured_output.getvalue().strip()

    def test_simple_word(self):
        """Testuje odwracanie prostego słowa."""
        output = self.run_script('Python')
        self.assertEqual(output, "Odwrócony tekst: nohtyP")

    def test_palindrome(self):
        """Testuje odwracanie palindromu."""
        output = self.run_script('kajak')
        self.assertEqual(output, "Odwrócony tekst: kajak")

    def test_sentence_with_spaces(self):
        """Testuje odwracanie zdania ze spacjami."""
        output = self.run_script('hello world')
        self.assertEqual(output, "Odwrócony tekst: dlrow olleh")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
