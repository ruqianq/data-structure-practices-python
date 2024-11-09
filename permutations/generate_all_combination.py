
def generate_all_combinations(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    unique_combinations = set()
    def helper(slate, i):
        if sum(slate) == target and i == len(arr):
            unique_combinations.add(tuple(slate))
            return
        if sum(slate) > target or i==len(arr):
            return
        helper(slate, i+1)
        slate.append(arr[i])
        helper(slate, i+1)
        slate.pop()
    helper([], 0)
    result = [list(comb) for comb in unique_combinations]
    return result


'''
    The function takes an INTEGER ARRAY and an INTEGER as inputs
    and is expected to return a 2D INTEGER ARRAY

    Complete the function below.
'''
def generate_all_combinations(arr, target):
    result = []

    def helper(slate, target, arr):
        if target == 0:
            result.append(slate[:])
            return
        if sum(arr) < target:
            return
        popped = None
        for i in range(len(arr)):
            if popped != arr[i]:
                if target - arr[i] >= 0:
                    slate.append(arr[i])
                    helper(slate, target - arr[i], arr[i + 1:])
                    popped = slate.pop()

    arr = sorted(arr, reverse=True)
    helper([], target, arr)
    return result


    def generate_all_combinations(arr, target):
    """
    Args:
     arr(list of int)
     target(int)
    Returns:
     list of list of int
    """
    arr.sort()  # Sort to handle duplicates
    result = []

    def helper(slate, i, current_sum):
        # If the current sum equals the target, add a copy of slate to result
        if current_sum == target:
            result.append(slate[:])
            return
        # If the sum exceeds the target or we've reached the end, return
        if current_sum > target or i == len(arr):
            return

        # Include the current element and move to the next element
        slate.append(arr[i])
        helper(slate, i + 1, current_sum + arr[i])
        slate.pop()  # Backtrack

        # Exclude the current element and skip any following duplicates of it
        while i + 1 < len(arr) and arr[i] == arr[i + 1]:
            i += 1
        helper(slate, i + 1, current_sum)

    helper([], 0, 0)
    return result
