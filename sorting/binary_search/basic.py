from typing import List


def binary_search(nums: List, target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = get_mid_upper(lo, hi)
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid


def get_mid_upper(lo: int, hi: int) -> int:
    return (lo + hi + 1)//2


def get_mid_lower(lo: int, hi: int) -> int:
    return (lo + hi)//2
