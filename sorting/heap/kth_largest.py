def kth_largest(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    import heapq

    len_stream = len(initial_stream)
    res = []
    heapq.heapify(initial_stream)
    curr_min = 0

    for i in range(len_stream - k + 1):
        curr_min = heapq.heappop(initial_stream)

    for j in append_stream:
        if j <= curr_min:
            res.append(curr_min)
        else:
            heapq.heappush(initial_stream, j)
            curr_min = heapq.heappop(initial_stream)
            res.append(curr_min)

    return res


# three way partitioning with quick sort
class Solution:
    def three_way_partition(self, arr, left, right, pivot_value):
        i = left

        while i <= right:
            if arr[i] < pivot_value:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
                i += 1
            elif arr[i] > pivot_value:
                arr[i], arr[right] = arr[right], arr[i]
                right -= 1
            else:
                i += 1
        return left, right
    
    def quick_select(self, arr, left, right, k):
        import random
        if left == right:
            return arr[left]
        
        pivot_index = random.randint(left, right)
        pivot_value = arr[pivot_index]

        lt, gt = self.three_way_partition(arr, left, right, pivot_value)

        if lt <= k <= gt:
            return arr[k]
        elif k < lt:
            return self.quick_select(arr, left, lt - 1, k)
        else:
            return self.quick_select(arr, gt+1, right, k)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        index_to_find = len(nums) - k
        return self.quick_select(nums, 0, len(nums) - 1, index_to_find)