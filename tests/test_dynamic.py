import unittest

from dynamic.can_sum import find_target_sum_ways
from dynamic.counting_bit import count_bits


class DynamicTest(unittest.TestCase):
    def test_min_path_sum(self):
        result = find_target_sum_ways([1, 1, 1, 1, 1], 3)
        self.assertEqual(result, 5)

    def test_countBits(self):
        result = count_bits(5)
        self.assertEqual(result, [0, 1, 1, 2, 1, 2])


if __name__ == '__main__':
    unittest.main()
