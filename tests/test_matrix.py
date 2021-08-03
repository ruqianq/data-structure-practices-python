import unittest

from matrix.matrix_reshape import matrix_reshape
from matrix.flood_fill import flood_fill


class TestMatrixModule(unittest.TestCase):
    def test_matrix_reshape_if_r_c_illegal(self):
        reshaped_matrix = matrix_reshape([[1, 2], [3, 4]], 1, 1)
        self.assertEqual(reshaped_matrix, [[1, 2], [3, 4]])

    def test_matrix_reshape_if_r_c_same_as_origin(self):
        reshaped_matrix = matrix_reshape([[1, 2, 0], [3, 4, 0]], 2, 3)
        self.assertEqual(reshaped_matrix, [[1, 2, 0], [3, 4, 0]])

    def test_matrix_reshape(self):
        reshaped_matrix = matrix_reshape([[1, 2, 0], [3, 4, 0]], 3, 2)
        self.assertEqual(reshaped_matrix, [[1, 2], [0, 3], [4, 0]])

    def test_matrix_reshape_r_c_bigger_than_m_n(self):
        reshaped_matrix = matrix_reshape([[1, 2], [3, 4]], 2, 4)
        self.assertEqual(reshaped_matrix, [[1, 2], [3, 4]])

    def test_flood_fill_new_color_equal_original_color(self):
        image = flood_fill([[1, 2], [3, 4]], 1, 1, 4)
        self.assertEqual(image, [[1, 2], [3, 4]])

    def test_flood_fill(self):
        image = flood_fill([[0,0,0],[0,0,0]], 0, 0, 2)
        self.assertEqual(image, [[2,2,2],[2,2,2]])


if __name__ == '__main__':
    unittest.main()
