# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the
# sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
# Dynamic Programming
from typing import List


# 1, create one grid called cost to store the calculated sum
# 2, as pointer move right calculated sum by adding prev cell (grid[0][j + 1],
# do the same thing for pointer moving down (grid[i+1][0]
# 3, for inner cells, loop over row and col, and add the min of upper neighbor and left neighbor
# 4, return the right bottom cell


def min_path_sum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    cost = [[0] * n for _ in range(m)]
    cost[0][0] = grid[0][0]
    for j in range(1, n):
        cost[0][j] = grid[0][j] + cost[0][j - 1]
    for i in range(1, m):
        cost[i][0] = grid[i][0] + cost[i - 1][0]
    for i in range(1, m):
        for j in range(1, n):
            cost[i][j] = min(cost[i - 1][j], cost[i][j - 1]) + grid[i][j]
    return cost[m - 1][n - 1]
