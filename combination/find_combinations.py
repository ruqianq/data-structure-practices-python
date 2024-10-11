from itertools import combinations

def find_combinations(n, k):
    """
    Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.

    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    arr = range(1, n+1)
    result = []

    def comb(n, k, li):
        if k == 0:
            result.append(li)
            return
        if n == 0:
            return
        comb(n-1, k-1, li + [arr[n-1]])
        comb(n-1, k, li)

    comb(n, k, [])
    return result
