import unittest

from binary_search.basic import get_mid_lower, get_mid_upper, binary_search
from binary_search.search_insert import search_insert


class TestBinarySearch(unittest.TestCase):
    def test_search_insert(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 7), 4)

    def test_search_insert_2(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 3), 1)

    def test_get_mid_upper(self):
        self.assertEqual(get_mid_upper(0, 3), 2)

    def test_get_mid_lower(self):
        self.assertEqual(get_mid_lower(0, 3), 1)

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 3, 5, 6], 6), 3)


if __name__ == '__main__':
    unittest.main()
