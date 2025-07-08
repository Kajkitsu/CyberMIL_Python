import unittest
import io
import runpy
import datetime
from unittest.mock import patch

class TestZad4(unittest.TestCase):

    def run_script(self, inputs, current_year):
        """Uruchamia skrypt z zadanym wiekiem i rokiem."""
        with patch('builtins.input', side_effect=inputs):
            with patch('datetime.date') as mock_date:
                # POPRAWKA:
                # Ustawiamy bezpośrednio atrybut .year na mocku, aby
                # wywołanie .year zwracało liczbę, a nie kolejny mock.
                mock_date.today.return_value.year = current_year

                captured_output = io.StringIO()
                with patch('sys.stdout', captured_output):
                    runpy.run_path('zad4.py', run_name='__main__')
                return captured_output.getvalue().strip().split('\n')

    def test_start_age_50(self):
        """Testuje pętlę dla wieku początkowego 50 lat."""
        output = self.run_script(['50'], 2024)
        self.assertEqual(len(output), 10)
        self.assertEqual(output[0], "W roku 2024 będziesz miał 50 lat.")
        self.assertEqual(output[9], "W roku 2033 będziesz miał 59 lat.")

    def test_start_age_22(self):
        """Testuje pętlę dla wieku początkowego 22 lat."""
        output = self.run_script(['22'], 2023)
        self.assertEqual(len(output), 10)
        self.assertEqual(output[0], "W roku 2023 będziesz miał 22 lat.")
        self.assertEqual(output[5], "W roku 2028 będziesz miał 27 lat.")

    def test_start_age_0(self):
        """Testuje pętlę dla wieku początkowego 0 lat."""
        output = self.run_script(['0'], 2025)
        self.assertEqual(len(output), 10)
        self.assertEqual(output[0], "W roku 2025 będziesz miał 0 lat.")
        self.assertEqual(output[9], "W roku 2034 będziesz miał 9 lat.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
