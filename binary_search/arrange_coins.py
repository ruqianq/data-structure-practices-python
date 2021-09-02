# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith
# row has exactly i coins. The last row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of the staircase you will build.

def calculate_sum(n: int) -> int:
    return (n * (n+1))//2


def arrange_coins(n: int) -> int:
    if n == 1:
        return 1
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi)//2
        if n == calculate_sum(mid):
            return mid
        elif n < calculate_sum(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo - 1
