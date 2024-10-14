def letter_case_permutations_immutable(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    # if it is letter, then need add upper/low (2 choices)
    # if it is digit add to the result
    # i = index of the char to decide on and S the string
    # partial problem the string generated so far
    result = []
    
    def helper(S, i, slate):
        # base case
        if i == len(S):
            result.append(slate)
            return
        else:
            if S[i].isdigit():
                helper(S, i+1, slate + S[i])
            else:
                helper(S, i+1, slate + S[i].upper())
                helper(S, i+1, slate + S[i].lower())
    helper(s, 0, "")
    return result


# Instead of creating a new string slate at every step in the recursion, you can modify the string in-place using a list. This avoids building new strings on every recursive call. Additionally, you can avoid storing all permutations at once by yielding results one at a time using a generator.

# This approach reduces auxiliary space by removing the need for constructing new strings at each recursive level and eliminates the need to store all results in memory simultaneously.

# Here’s how you could implement it:

def letter_case_permutations_mutation(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    # if it is letter, then need add upper/low (2 choices)
    # if it is digit add to the result
    # i = index of the char to decide on and S the string
    # partial problem the string generated so far
    result = []
    s = list(s)  # Convert to a list for in-place modification
    
    def backtrack(i):
        if i == len(s):
            result.append("".join(s))
            return
        else:
            if s[i].isalpha():
                # Choose lower case
                s[i] = s[i].lower()
                backtrack(i + 1)
                
                # Choose upper case
                s[i] = s[i].upper()
                backtrack(i + 1)
            else:
                # If digit, just move forward
                backtrack(i + 1)
    backtrack(0)
            
    return result
