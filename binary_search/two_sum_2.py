# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they
# add up to a specific target number.
#
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
# where 1 <= answer[0] < answer[1] <= numbers.length.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1
