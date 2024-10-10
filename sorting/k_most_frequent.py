import heapq
from collections import Counter


def k_most_frequent(k, words):
    """
    Given a number and a list of words, return the given number of most frequent words.

{
"k": 4,
"words": ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]
}

["car", "driver", "taxi", "bus"]

Every word consists of only lowercase English letters.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

    Args:
     k(int32)
     words(list_str)
    Returns:
     list_str
    """
    # Write your code here.

    hash_table = {}
    for word in words:
        if word in hash_table:
            hash_table[word] += 1
        else:
            hash_table[word] = 1
    hash_table = dict(sorted(hash_table.items(), key=lambda item: item[0], reverse=True))
    return list(hash_table.keys())[:k]


def find_top_k_frequent_elements(arr, k):
    """
    Given an integer array and a number k, find the k most frequent elements in the array.

    Args:
     arr(list_int32)
     k(int32)
     {
"arr": [1, 2, 3, 2, 4, 3, 1],
"k": 2
}

[3, 1]

    Returns:
     list_int32
    """
    # Write your code here.

    # build the hash table
    counts = Counter(arr)

    # build the heap
    heap = []

    for element, freq in counts.items():
            # 3: Manage the heap
            # Add each element to the heap
        heapq.heappush(heap, (freq, element))
            # If the size of the heap is larger than k, we pop the element at the top. 
        if len(heap) > k:
            heapq.heappop(heap)
        
        # 4: What remains in the heap are the top k most frequent
    return [num for (count, num) in heap]

