# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
from typing import List


class Solution:
    def update_matrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        from collections import deque
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            for dirr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newX, newY = x + dirr[0], y + dirr[1]
                if newX >= 0 and newX <= len(mat) - 1 and newY >= 0 and newY <= len(mat[0]) - 1 and (
                        newX, newY) not in visited:
                    mat[newX][newY] = mat[x][y] + 1
                    visited.add((newX, newY))
                    q.append((newX, newY))
        return mat
