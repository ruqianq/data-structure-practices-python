def segregate_evens_and_odds(numbers):
    """
    Given an array of numbers, rearrange them in-place so that even numbers appear before odd ones.
    It is important to practice solving this problem by rearranging numbers in-place.
    There is no need to preserve the original order within the even and within the odd numbers.
    We look for a solution of the linear time complexity that uses constant auxiliary space.
    Args:
        numbers (list_int32): List of numbers to be rearranged
    Returns:
        list_int32: Rearranged list of numbers
    """
    low = 0
    high = len(numbers) - 1
    
    while low < high:
        if numbers[low] % 2 == 0:
            low += 1
        else:
            if numbers[high] % 2 == 0:
                numbers[low], numbers[high] = numbers[high], numbers[low]
                low += 1
            high -= 1
    
    return numbers
