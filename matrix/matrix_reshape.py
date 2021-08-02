from typing import List


def matrix_reshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    if m * n <= r * c and (r != m or c != n):
        return [[]]
    return mat
