def get_permutations_unique(arr):
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


def get_permutations_unique_swap(arr):
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