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


def find_combinations_mutable(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = [] 
    slate = []
    def helper(i):
        if len(slate) == k:
            result.append(slate[:])
            return
        else:
            for j in range(i, n+1):
                slate.append(j)
                helper(j+1)
                slate.pop()
    helper(1)
    return result

 
def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    r=[]
    def permutations(s,n):
        if len(n)==0:
            r.append(s[:])
            return
        else:
            for i in range(0,len(n)):
                s.append(n[i])
                permutations(s,n[:i]+n[i+1:])
                s.pop()
    permutations([],arr)    
    return r


def get_permutations_swap(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Store the result list
    result = []
    
    # Helper function for recursion
    def helper(i):
        # Base case: if all elements have been processed
        if i == len(arr):
            result.append(arr[:])  # Add a copy of the current permutation to the result
        else:
            # Iterate over the remaining elements to generate permutations
            for j in range(i, len(arr)):
                # Swap to fix the current element
                arr[i], arr[j] = arr[j], arr[i]
                # Recurse for the next position
                helper(i+1)
                # Backtrack by swapping the elements back
                arr[i], arr[j] = arr[j], arr[i]

    # Start the recursion from index 0
    helper(0)
    
    return result    