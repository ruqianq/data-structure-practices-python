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
