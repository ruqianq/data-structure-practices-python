# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
# Dynamic Programming
from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    M, N = len(grid), len(grid[0])
    cost = [[0]*N for _ in range(M)]
    cost[0][0] = grid[0][0]
    for j in range(1,N):
        cost[0][j] = grid[0][j] + cost[0][j-1]
    for i in range(1,M):
        cost[i][0] = grid[i][0] + cost[i-1][0]
    for i in range(1,M):
        for j in range(1,N):
            cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]
    return cost[M-1][N-1]
