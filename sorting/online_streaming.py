import heapq

def online_median(stream):
    """
    Args:
     stream(list_int32): A list of integers representing the stream of numbers.
    Returns:
     list_int32: A list of medians calculated after each number in the stream.
    """
    res = []  # List to store the medians
    
    minh = []  # Min heap to store the larger half of the numbers
    maxh = []  # Max heap to store the smaller half of the numbers
    median = 0.0  # Variable to store the current median
    
    for num in stream:
        if num > median:
            heapq.heappush(minh, num)  # Push the number to the min heap
            if len(minh) - len(maxh) == 2:
                heapq.heappush(maxh, -heapq.heappop(minh))  # Balance the heaps if necessary
        else:
            heapq.heappush(maxh, -num)  # Push the negated number to the max heap
            if len(maxh) - len(minh) == 2:
                heapq.heappush(minh, -heapq.heappop(maxh))  # Balance the heaps if necessary
        
        if len(minh) == len(maxh):
            median = (minh[0] - maxh[0]) // 2  # Calculate the median if the heaps have equal size
        elif len(minh) > len(maxh):
            median = minh[0]  # Calculate the median using the top element of the min heap
        else:
            median = -maxh[0]  # Calculate the median using the negated top element of the max heap

        res.append(median)  # Append the median to the result list
    
    return res
