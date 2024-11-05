def find_zero_sum(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_str
    """
    # Write your code here.
    arr.sort()
    result = set()
    if len(arr) < 3:
        return []
    for p1 in range(len(arr) - 2):
        p2 = p1 + 1
        p3 = len(arr) - 1
        while p2 < p3:
            if arr[p1] + arr[p2] + arr[p3] == 0:
                
                result.add((arr[p1],arr[p2], arr[p3]))
                p2 += 1
                p3 -= 1
            elif arr[p1] + arr[p2] + arr[p3] < 0:
                p2 += 1
            else:
                p3 -= 1
    return [f'{x},{y},{z}' for x, y, z in result]
    