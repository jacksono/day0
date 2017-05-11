
import unittest
from prime_numbers import prime_numbers

class TestPrimeNumbers(unittest.TestCase):
    '''
    Tests for the prime_numbers() function
    '''
    def test_input_not_empty(self):
        with self.assertRaises(TypeError):
            prime_numbers()

    def test_input_not_less_than_0(self):
        self.assertEqual('Invalid input, negative number entered', prime_numbers(-3))

    def test_input_is_string(self):
        self.assertEqual('Invalid input type', prime_numbers('str'))

    def test_input_is_float(self):
        self.assertEqual('Invalid input type', prime_numbers(10.3))

    def test_input_is_list(self):
        self.assertEqual('Invalid input type', prime_numbers([1,2]))

    def test_input_is_dictionary(self):
        self.assertEqual('Invalid input type', prime_numbers({1:'a'}))

    def test_input_is_set(self):
        self.assertEqual('Invalid input type', prime_numbers(set()))

    def test_output_is_a_list(self):
        self.assertEqual(list, type(prime_numbers(3)))

    def test_correct_output_for_input_5(self):
        self.assertEqual([2,3,5], prime_numbers(5))

    def test_output_not_beyond_the_range_if_n_is_a_prime_number(self):
        self.assertTrue(prime_numbers(5)[-1] <= 5)

    def test_output_not_beyond_the_range_if_n_is_not_a_prime_number(self):
        self.assertTrue(prime_numbers(8)[-1] <= 8)
