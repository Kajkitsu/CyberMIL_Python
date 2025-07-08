import unittest
import io
import runpy
import datetime
from unittest.mock import patch

class TestZad2(unittest.TestCase):

    def run_script(self, inputs, current_year):
        """Uruchamia skrypt, mockując datę i dane wejściowe."""
        with patch('builtins.input', side_effect=inputs):
            with patch('datetime.date') as mock_date:
                # POPRAWKA:
                # Zamiast zwracać cały obiekt daty, konfigurujemy mock tak, aby
                # wywołanie .year na obiekcie zwróconym przez .today()
                # dało konkretną liczbę (rok).
                mock_date.today.return_value.year = current_year

                captured_output = io.StringIO()
                with patch('sys.stdout', captured_output):
                    runpy.run_path('zad2.py', run_name='__main__')
                return captured_output.getvalue().strip().split('\n')

    def test_case_1(self):
        """Testuje dla wieku 30 lat w roku 2024."""
        output = self.run_script(['Tester', '30'], 2024)
        self.assertIn("Cześć jestem Tester, mam 30 lat.", output[0])
        self.assertIn("Urodziłeś się w 1994 roku.", output[1])

    def test_case_2(self):
        """Testuje dla wieku 1 roku w roku 2025."""
        output = self.run_script(['Dziecko', '1'], 2025)
        self.assertIn("Cześć jestem Dziecko, mam 1 lat.", output[0])
        self.assertIn("Urodziłeś się w 2024 roku.", output[1])

    def test_case_3(self):
        """Testuje dla wieku 0 lat w roku 2023."""
        output = self.run_script(['Noworodek', '0'], 2023)
        self.assertIn("Cześć jestem Noworodek, mam 0 lat.", output[0])
        self.assertIn("Urodziłeś się w 2023 roku.", output[1])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
