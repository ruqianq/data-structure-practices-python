import unittest

from dynamic.can_sum import find_target_sum_ways


class DynamicTest(unittest.TestCase):
    def test_min_path_sum(self):
        result = find_target_sum_ways([1, 1, 1, 1, 1], 3)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
