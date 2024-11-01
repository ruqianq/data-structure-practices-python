def kth_largest_in_an_array(numbers, k):
    """
    Args:
     numbers (list): List of integers
     k (int): Position of the largest element to find
    Returns:
     int: The k-th largest element in the array
    """
    import heapq
    k_largest = 0
    minHeap = False
    
    # Step 1: Decide between using a min-heap or max-heap
    if k > len(numbers) // 2:
        # If k is more than half the size of the array, use a min-heap
        # Convert the problem into finding the (n - k + 1) smallest element
        minHeap = True
        k = len(numbers) - k + 1
    
    # Step 2: Use the selected heap type to find the k-th largest
    if minHeap:
        # Min-heap for finding the (n - k + 1)-smallest (equivalent to k-th largest)
        heapq.heapify(numbers)  # Transform list into a min-heap in-place
        for i in range(k):
            # Pop the smallest element in the min-heap k times
            k_largest = heapq.heappop(numbers)
    else:
        # Max-heap for finding the k-th largest directly
        heapq._heapify_max(numbers)  # Transform list into a max-heap
        for i in range(k):
            # Pop the largest element in the max-heap k times
            k_largest = heapq._heappop_max(numbers)
    
    return k_largest


def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = nums[:k]
        heapq.heapify(heap)

        for n in nums[k:]:
            if n > heap[0]:
                heapq.heappushpop(heap, n)
        return heap[0]
