def get_permutations_unique(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Store the result list
    result = []
    
    def permutations_helper(current_permutation, remaining_elements):
        if len(remaining_elements) == 0:
            result.append(current_permutation[:])
            return
        else:
            for i in range(0, len(remaining_elements)): # only have n - i choice to choose for each worker
                current_permutation.append(remaining_elements[i])
                permutations_helper(current_permutation, remaining_elements[:i] + remaining_elements[i+1:])
                #backtrack, resume current_permuation to the previous state
                current_permutation.pop()
    
    permutations_helper([], arr)
    
    return result


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
                # Swap to fix the current element, because we need to fill the left-most black of subproblem
                arr[i], arr[j] = arr[j], arr[i]
                # Recurse for the next position
                helper(i+1)
                # Backtrack by swapping the elements back, whatever we swap we need to unswap it
                arr[i], arr[j] = arr[j], arr[i]

    # Start the recursion from index 0
    helper(0)
    
    return result    