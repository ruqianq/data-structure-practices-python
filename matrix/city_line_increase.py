# Max Increase to Keep City Skyline
#
# There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.
#
# A city's skyline is the the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different.
#
# We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.
#
# Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.
from typing import List


def max_increase_keeping_skyline(grid: List[List[int]]) -> int:
    cols_max = []
    for j in range(len(grid[0])):
        col_wise = []
        for i in range(len(grid)):
            col_wise.append(grid[i][j])
        cols_max.append(max(col_wise))
    sum = 0
    for i in range(len(grid)):
        row_max = max(grid[i])
        for j in range(len(grid[i])):
            diff = min(row_max, cols_max[j]) - grid[i][j]
            sum += diff
    return sum


# Clean
def max_increase_keeping_skyline_cln(grid: List[List[int]]) -> int:
    row, col = map(max, grid), map(max, zip(*grid))
    return sum(min(i, j) for i in row for j in col) - sum(map(sum, grid))




