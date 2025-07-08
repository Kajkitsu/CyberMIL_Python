import unittest
import io
import runpy
from unittest.mock import patch

class TestZad5(unittest.TestCase):

    def run_script(self, celsius_input):
        """Uruchamia skrypt konwertujący temperaturę."""
        with patch('builtins.input', return_value=celsius_input):
            captured_output = io.StringIO()
            with patch('sys.stdout', captured_output):
                runpy.run_path('zad5.py', run_name='__main__')
            return captured_output.getvalue().strip()
    
    def test_zero_celsius(self):
        """Testuje konwersję 0°C na 32°F."""
        output = self.run_script('0')
        self.assertIn("0.0°C to 32.0°F", output)

    def test_100_celsius(self):
        """Testuje konwersję 100°C na 212°F."""
        output = self.run_script('100')
        self.assertIn("100.0°C to 212.0°F", output)

    def test_negative_celsius(self):
        """Testuje konwersję -10°C na 14°F."""
        output = self.run_script('-10')
        self.assertIn("-10.0°C to 14.0°F", output)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
