def segregate_evens_and_odds(numbers):
    """
    Given an array of numbers, rearrange them in-place so that even numbers appear before odd ones.
    It is important to practice solving this problem by rearranging numbers in-place.
    There is no need to preserve the original order within the even and within the odd numbers.
    We look for a solution of the linear time complexity that uses constant auxiliary space.
    Args:
        numbers(list_int32)
        {
            "numbers": [1, 2, 3, 4]
        }
    Returns:
        list_int32
        [4, 2, 3, 1]
    """
    # Write your code here.
    for n in numbers:
        for i in range(n+1, len(numbers) - 1):
            if numbers[i] % 2 == 0:
                numbers[n], numbers[i] = numbers[i], numbers[n]
                break
    return numbers



