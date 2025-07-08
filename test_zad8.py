import unittest
import io
import runpy
from unittest.mock import patch

class TestZad8(unittest.TestCase):

    def run_script(self, number_input):
        """Uruchamia skrypt sprawdzający liczby pierwsze."""
        with patch('builtins.input', return_value=number_input):
            captured_output = io.StringIO()
            with patch('sys.stdout', captured_output):
                runpy.run_path('zad8.py', run_name='__main__')
            return captured_output.getvalue().strip()

    def test_is_prime(self):
        """Testuje dla liczby pierwszej (7)."""
        output = self.run_script('7')
        self.assertEqual(output, "Liczba 7 jest liczbą pierwszą.")

    def test_is_not_prime(self):
        """Testuje dla liczby złożonej (10)."""
        output = self.run_script('10')
        self.assertEqual(output, "Liczba 10 nie jest liczbą pierwszą.")

    def test_edge_case_one(self):
        """Testuje dla przypadku brzegowego (1)."""
        output = self.run_script('1')
        self.assertEqual(output, "Liczba 1 nie jest liczbą pierwszą.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
