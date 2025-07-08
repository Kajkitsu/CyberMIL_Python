import unittest
import io
import runpy
import datetime
from unittest.mock import patch

class TestZad3(unittest.TestCase):

    def run_script(self, inputs):
        """Uruchamia skrypt i zwraca jego wynik jako listę linii."""
        with patch('builtins.input', side_effect=inputs):
            captured_output = io.StringIO()
            with patch('sys.stdout', captured_output):
                # Mockujemy datę, aby zapewnić spójność działania
                with patch('datetime.date') as mock_date:
                    mock_date.today.return_value = datetime.date(2024, 1, 1)
                    runpy.run_path('zad3.py', run_name='__main__')
            return captured_output.getvalue().strip().split('\n')

    def test_under_26(self):
        """Testuje dla wieku poniżej 26 lat (zwolnienie z podatku)."""
        output = self.run_script(['Student', '25'])
        self.assertEqual(output[-1], "Jesteś zwolniony/a z podatku dochodowego.")

    def test_at_26(self):
        """Testuje dla wieku 26 lat (brak zwolnienia)."""
        output = self.run_script(['Pracownik', '26'])
        self.assertEqual(output[-1], "Nie jesteś zwolniony/a z podatku dochodowego.")

    def test_over_26(self):
        """Testuje dla wieku powyżej 26 lat (brak zwolnienia)."""
        output = self.run_script(['Senior', '67'])
        self.assertEqual(output[-1], "Nie jesteś zwolniony/a z podatku dochodowego.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
