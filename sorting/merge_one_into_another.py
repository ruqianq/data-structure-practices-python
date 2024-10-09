def merge_one_into_another(first, second):
    """
    First array has n positive numbers, and they are sorted in the non-descending order.

Second array has 2n numbers: first n are also positive and sorted in the same way but the last n are all zeroes.

Merge the first array into the second and return the latter. You should get 2n positive integers sorted in the non-descending order.

    Args:
     first(list_int32)
     second(list_int32)
     {
"first": [1, 3, 5],
"second": [2, 4, 6, 0, 0, 0]
}
    Returns:
     list_int32
     [1, 2, 3, 4, 5, 6]
    """
    # Write your code here.
    def merge_one_into_another(first, second):
        """
        First array has n positive numbers, and they are sorted in the non-descending order.

    Second array has 2n numbers: first n are also positive and sorted in the same way but the last n are all zeroes.

    Merge the first array into the second and return the latter. You should get 2n positive integers sorted in the non-descending order.

        Args:
         first(list_int32)
         second(list_int32)
         {
    "first": [1, 3, 5],
    "second": [2, 4, 6, 0, 0, 0]
    }
        Returns:
         list_int32
         [1, 2, 3, 4, 5, 6]
        """
        # Write your code here.
        i = len(first) - 1
        j = len(second) - 1

        while i >= 0 and j >= 0:
            if first[i] > second[j]:
                second[j] = first[i]
                i -= 1
            else:
                second[j] = second[j]
                j -= 1
        second.sort()
        return second
