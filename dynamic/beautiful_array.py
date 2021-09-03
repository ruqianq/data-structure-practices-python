# For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:
#
# For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].
#
# Given n, return any beautiful array nums.  (It is guaranteed that one exists.)
# pattern is create the odd list = 2*i - 1 and even list = 2*i and using the previous list to loop
from typing import List


def beautiful_array(n: int) -> List[int]:
    result = [1]
    while len(result) < n:
        result = [i * 2 - 1 for i in result] + [i * 2 for i in result]
    return [i for i in result if i <= n]
