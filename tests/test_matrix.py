import unittest

from matrix.matrix_reshape import matrix_reshape


class TestMatrixModule(unittest.TestCase):
    def test_matrix_reshape_if_r_c_illegal(self):
        reshaped_matrix = matrix_reshape([[1, 2], [3, 4]], 1, 1)
        self.assertEqual(reshaped_matrix, [[1, 2], [3, 4]])


if __name__ == '__main__':
    unittest.main()
