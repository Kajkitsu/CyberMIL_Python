import unittest
import io
import runpy
from unittest.mock import patch

class TestZad11(unittest.TestCase):

    def run_script(self, number_input):
        """Uruchamia skrypt sumujący liczby parzyste."""
        with patch('builtins.input', return_value=number_input):
            captured_output = io.StringIO()
            with patch('sys.stdout', captured_output):
                runpy.run_path('zad11.py', run_name='__main__')
            return captured_output.getvalue().strip()

    def test_even_limit(self):
        """Testuje dla parzystej liczby granicznej (10)."""
        output = self.run_script('10')
        self.assertEqual(output, "Suma liczb parzystych od 0 do 10 wynosi: 30")

    def test_odd_limit(self):
        """Testuje dla nieparzystej liczby granicznej (9)."""
        output = self.run_script('9')
        self.assertEqual(output, "Suma liczb parzystych od 0 do 9 wynosi: 20")

    def test_zero_limit(self):
        """Testuje dla liczby granicznej równej 0."""
        output = self.run_script('0')
        self.assertEqual(output, "Suma liczb parzystych od 0 do 0 wynosi: 0")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
