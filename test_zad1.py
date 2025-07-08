import unittest
import io
import runpy
from unittest.mock import patch

class TestZad1(unittest.TestCase):

    def run_script(self, inputs):
        """Uruchamia skrypt z zadanymi danymi wejściowymi i zwraca jego wynik."""
        with patch('builtins.input', side_effect=inputs):
            captured_output = io.StringIO()
            with patch('sys.stdout', captured_output):
                runpy.run_path('zad1.py', run_name='__main__')
            return captured_output.getvalue().strip()

    def test_standard_input(self):
        """Testuje typowe dane wejściowe."""
        output = self.run_script(['Anna', '25'])
        self.assertEqual(output, "Cześć jestem Anna, mam 25 lat.")

    def test_different_input(self):
        """Testuje inny zestaw danych."""
        output = self.run_script(['Piotr', '40'])
        self.assertEqual(output, "Cześć jestem Piotr, mam 40 lat.")

    def test_name_with_space(self):
        """Testuje imię zawierające spację."""
        output = self.run_script(['Jan Kowalski', '30'])
        self.assertEqual(output, "Cześć jestem Jan Kowalski, mam 30 lat.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
