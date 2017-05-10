import unittest
from generate_prime_numbers import generate_primes

class test_prime_numbers(unittest.TestCase):
    def test_invalid_input(self):
        self.assertEquals(generate_primes('sha6'), 'Invalid input!Enter a digit')
    def test_for_correct_output(self):
        self.assertEquals(generate_primes(9),[2,3,5,7])
    def test_for_negative_input(self):
        self.assertEquals(generate_primes(-1), 'Negative numbers are not permited')
    def test_2(self):
        self.assertFalse(generate_primes(2), False)
    def test_1(self):
        self.assertFalse(generate_primes(1), False)
    def test_0(self):
        self.assertFalse(generate_primes(0), False)
    def test_7(self):
        self.assertTrue(generate_primes(7),True)
 

if __name__== "__main__":
    unittest.main()
