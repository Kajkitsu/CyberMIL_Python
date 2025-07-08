import unittest
import io
import runpy
from unittest.mock import patch

class TestZad13(unittest.TestCase):

    def run_script(self, number_input):
        """Uruchamia skrypt do konwersji systemów liczbowych."""
        with patch('builtins.input', return_value=number_input):
            captured_output = io.StringIO()
            with patch('sys.stdout', captured_output):
                runpy.run_path('zad13.py', run_name='__main__')
            return captured_output.getvalue().strip().split('\n')

    def test_number_10(self):
        """Testuje konwersję liczby 10."""
        output = self.run_script('10')
        self.assertEqual(output[0], "Binarnie: 1010")
        self.assertEqual(output[1], "Ósemkowo: 12")
        self.assertEqual(output[2], "Szesnastkowo: A")

    def test_number_255(self):
        """Testuje konwersję liczby 255."""
        output = self.run_script('255')
        self.assertEqual(output[0], "Binarnie: 11111111")
        self.assertEqual(output[1], "Ósemkowo: 377")
        self.assertEqual(output[2], "Szesnastkowo: FF")

    def test_number_0(self):
        """Testuje konwersję liczby 0."""
        output = self.run_script('0')
        self.assertEqual(output[0], "Binarnie: 0")
        self.assertEqual(output[1], "Ósemkowo: 0")
        self.assertEqual(output[2], "Szesnastkowo: 0")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
