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
    arr.sort()  # Sort the array in ascending order
    result = []  # Initialize an empty list to store the quadruples
    n = len(arr)  # Get the length of the array
    for num1 in range(n - 3):  # Iterate through the array up to the third-to-last element
        if arr[num1] == arr[num1-1] and num1 > 0:  # Skip duplicates of the first number
            continue
        for num2 in range(num1 + 1, n - 2):  # Iterate through the array starting from the second number
            if num2 > num1 + 1 and arr[num2] == arr[num2-1]:  # Skip duplicates of the second number
                continue
            left = num2 + 1  # Set the left pointer to the next element after the second number
            right = n - 1  # Set the right pointer to the last element
            while left < right:  # Iterate until the pointers meet
                if arr[num1] + arr[num2] + arr[left] + arr[right] == target:  # Check if the sum is equal to the target
                    result.append([arr[num1], arr[num2], arr[left], arr[right]])  # Add the quadruple to the result list
                    while left < right and arr[left] == arr[left+1]:  # Skip duplicates of the third number
                        left += 1
                    while left < right and arr[right] == arr[right-1]:  # Skip duplicates of the fourth number
                        right -= 1
                    left += 1  # Move the left pointer to the next element
                    right -= 1  # Move the right pointer to the previous element
                elif arr[num1] + arr[num2] + arr[left] + arr[right] < target:  # If the sum is less than the target, move the left pointer to the next element
                    left += 1
                else:  # If the sum is greater than the target, move the right pointer to the previous element
                    right -= 1

    return result  # Return the list of unique quadruples that sum up to the target value