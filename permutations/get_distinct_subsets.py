
# Complete the function below. 
# The function accepts a STRING as parameter and is expected to return a STRING ARRAY.
def get_distinct_subsets(s):
    s = ''.join(sorted(s))
    res = [""]
    for char in s: 
        curr_size = len(res)
        for i in range(curr_size): 
            curr_str = res[i]
            if char in curr_str:
                res[i] = curr_str+char
            else:
                res.append(curr_str+char)
            
    return res

def get_distinct_subsets(s: str) -> List[str]:
    """
    Args:
     s (str): Input string
    Returns:
     List[str]: List of distinct subsets
    """
    # Sort the input string to handle duplicates easily
    result = set()
    
    def helper(slate, i):
        # Base case: if we've processed all characters
        if i == len(s):
            sorted_slate = ''.join(sorted(slate))
            result.add(sorted_slate)
            return
        
        # Exclude the current character
        helper(slate, i + 1)
        
        # Include the current character only if it's the first of its duplicates
        #if i == 0 or s[i] != s[i - 1]:
        helper(slate + s[i], i + 1)

    helper('', 0)
    final = list(result)
    return final
