def count_triplets(target, numbers):
    """
    Given a list of numbers, count the number of triplets having a sum less than a given target.

{
"target": 4,
"numbers": [5, 0, -1, 3, 2]
}
2
    Args:
     target(int32)
     numbers(list_int32)
    Returns:
     int32
     
    """
    # Write your code here.
    numbers.sort()
    p1 = 0
    count = 0
    for p1 in range(len(numbers) - 2):
        p2 = p1 + 1
        p3 = len(numbers) - 1
        while p2 < p3:
            if numbers[p1] + numbers[p2] + numbers[p3] < target:
                count += p3 - p2
                p2 += 1
            else:
                p3 -= 1
    return count
