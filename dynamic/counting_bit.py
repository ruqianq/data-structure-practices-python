# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i]
# is the number of 1's in the binary representation of i.

# Fib
from typing import List


def count_bits(n: int) -> List[int]:
    ans = [0, 1]
    while len(ans) <= n:
        for num in ans[:]:
            ans.append(num + 1)
    return ans[:n + 1]
