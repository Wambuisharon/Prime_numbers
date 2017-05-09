import unittest
from generate_prime_numbers import generate_prime

class test_prime_numbers(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEquals(generate_primes('sha6'), 'Invalid input!Enter a digit')
    def test_for_correct_output(self):
        self.assertEquals(generate_primes(9),[2,3,5,7])
    def test_for_negative_input(self):
        self.assertEquals(generate_primes(-1), 'Negative numbers are not permited')

if __name__== "__main__":
    unittest.main()