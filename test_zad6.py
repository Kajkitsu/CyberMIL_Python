import unittest
import io
import runpy
from unittest.mock import patch

class TestZad6(unittest.TestCase):

    def setUp(self):
        """Uruchamia skrypt FizzBuzz i zapisuje wynik przed każdym testem."""
        captured_output = io.StringIO()
        with patch('sys.stdout', captured_output):
            runpy.run_path('zad6.py', run_name='__main__')
        self.lines = captured_output.getvalue().strip().split('\n')

    def test_fizz_output(self):
        """Sprawdza, czy dla liczby 3 wypisywane jest 'Fizz'."""
        self.assertEqual(self.lines[2], "Fizz")  # Indeks 2 odpowiada liczbie 3

    def test_buzz_output(self):
        """Sprawdza, czy dla liczby 5 wypisywane jest 'Buzz'."""
        self.assertEqual(self.lines[4], "Buzz")  # Indeks 4 odpowiada liczbie 5

    def test_fizzbuzz_output(self):
        """Sprawdza, czy dla liczby 15 wypisywane jest 'FizzBuzz'."""
        self.assertEqual(self.lines[14], "FizzBuzz") # Indeks 14 odpowiada liczbie 15

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
