import unittest
from sorting.segregate_evens_and_odds import segregate_evens_and_odds

class TestSegregateEvensAndOdds(unittest.TestCase):

    def test_segregate_evens_and_odds(self):
        numbers = [1, 2, 3, 4]
        expected_result = [4, 2, 3, 1]
        self.assertEqual(segregate_evens_and_odds(numbers), expected_result)

    def test_segregate_evens_and_odds_with_empty_list(self):
        numbers = []
        expected_result = []
        self.assertEqual(segregate_evens_and_odds(numbers), expected_result)

    def test_segregate_evens_and_odds_with_all_even_numbers(self):
        numbers = [2, 4, 6, 8]
        expected_result = [2, 4, 6, 8]
        self.assertEqual(segregate_evens_and_odds(numbers), expected_result)

    def test_segregate_evens_and_odds_with_all_odd_numbers(self):
        numbers = [1, 3, 5, 7]
        expected_result = [1, 3, 5, 7]
        self.assertEqual(segregate_evens_and_odds(numbers), expected_result)

    def test_segregate_evens_and_odds_with_mixed_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_result = [8, 2, 6, 4, 5, 3, 7, 1, 9]
        self.assertEqual(segregate_evens_and_odds(numbers), expected_result)

if __name__ == '__main__':
    unittest.main()