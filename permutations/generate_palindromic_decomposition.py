
def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    result = []
    def helper(slate, start):
        if start == len(s):  
            result.append("|".join(slate[:]))
            return
        for end in range(start + 1, len(s) + 1):  # Notice end starts from start + 1
            sub = s[start:end]
            if sub == sub[::-1]:  # Only proceed if the substring is a palindrome
                slate.append(sub)
                helper(slate, end)  # Move to the next start position
                slate.pop()         # Backtrack to try other decompositions
    
    helper([],0)
    
    
    return result

    