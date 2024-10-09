
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
 
