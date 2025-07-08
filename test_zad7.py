import unittest
import io
import runpy
from unittest.mock import patch

class TestZad7(unittest.TestCase):

    def run_script(self, inputs):
        """Uruchamia skrypt obliczający BMI."""
        with patch('builtins.input', side_effect=inputs):
            captured_output = io.StringIO()
            with patch('sys.stdout', captured_output):
                runpy.run_path('zad7.py', run_name='__main__')
            return captured_output.getvalue().strip()

    def test_normal_bmi(self):
        """Testuje przypadek prawidłowego BMI."""
        output = self.run_script(['70', '1.75'])
        self.assertEqual(output, "Twoje BMI wynosi: 22.86")

    def test_overweight_bmi(self):
        """Testuje przypadek nadwagi."""
        output = self.run_script(['90', '1.75'])
        self.assertEqual(output, "Twoje BMI wynosi: 29.39")

    def test_underweight_bmi(self):
        """Testuje przypadek niedowagi."""
        output = self.run_script(['50', '1.80'])
        self.assertEqual(output, "Twoje BMI wynosi: 15.43")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
