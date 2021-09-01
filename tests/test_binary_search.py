import unittest

from binary_search.search_insert import search_insert


class TestBinarySearch(unittest.TestCase):
    def test_search_insert(self):
        self.assertEqual(search_insert([1, 3, 5, 6], 7), 4)


if __name__ == '__main__':
    unittest.main()
