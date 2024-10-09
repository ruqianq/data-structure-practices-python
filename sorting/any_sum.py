def find_zero_sum(arr):
    """
    Given an integer array arr of size n, find all magic triplets in it.

Magic triplet is a group of three numbers whose sum is zero.

Note that magic triplets may or may not be made of consecutive numbers in arr.

Function must return an array of strings. Each string (if any) in the array must represent a unique magic triplet and strictly follow this format: "1,2,-3" (no whitespace, one comma between numbers).
Order of the strings in the array is insignificant. Order of the integers in any string is also insignificant. For example, if ["1,2,-3", "1,-1,0"] is a correct answer, then ["0,1,-1", "1,-3,2"] is also a correct answer.
Triplets that only differ by order of numbers are considered duplicates, and duplicates must not be returned. For example, if "1,2,-3" is a part of an answer, then "1,-3,2", "-3,2,1" or any permutation of the same numbers may not appear in the same answer (though any one of them may appear instead of "1,2,-3").
Constraints:

1 <= n <= 2000
-1000 <= any element of arr <= 1000
arr may contain duplicate numbers
arr is not necessarily sorted
    Args:
     arr(list_int32)
     {
"arr": [10, 3, -4, 1, -6, 9]
}
    Returns:
     list_str
     ["10,-4,-6", "3,-4,1"]

    """
    # Write your code here.

    arr.sort()
    result = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i + 1
        right = len(arr) - 1
        while left < right:
            if arr[i] + arr[left] + arr[right] == 0:
                result.append(f"{arr[i]},{arr[left]},{arr[right]}")
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif arr[i] + arr[left] + arr[right] < 0:   
                left += 1
            else:
                right -= 1

    return result


def four_sum(arr, target):
    """
    Given a list of numbers, find all the unique quadruples that sum up to a given target value.
Two quadruples are considered different if there exists a number whose frequencies differ in those two quadruples.
The quadruples can be returned in any order.
The order of numbers inside any quadruple does not matter.
    Args:
     arr(list_int32)
     target(int32)
     {
"arr": [0, 0, 1, 3, 2, -1],
"target": 3
}
    Returns:
     list_list_int32
    """
    arr.sort()
    result = []
    n = len(arr)
    for num1 in range(n - 3):
        if arr[num1] == arr[num1-1] and num1 > 0:
            continue
        for num2 in range(num1 + 1, n - 2):
            if num2 > num1 + 1 and arr[num2] == arr[num2-1]:
                continue
            left = num2 + 1
            right = n - 1
            while left < right:
                if arr[num1] + arr[num2] + arr[left] + arr[right] == target:
                    result.append([arr[num1], arr[num2], arr[left], arr[right]])
                    while left < right and arr[left] == arr[left+1]:
                        left += 1
                    while left < right and arr[right] == arr[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif arr[num1] + arr[num2] + arr[left] + arr[right] < target:
                    left += 1
                else:
                    right -= 1

    return result