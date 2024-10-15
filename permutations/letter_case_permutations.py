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

# here is the mutable version of the code
# we need to use a slate to store the current permutation and we need to use a helper function to do the recursion, treat the slate as a stack.

def letter_case_permutations_mutable(s):
    """
    Args:
     s(str): The input string
    Returns:
     list_str: List of all letter case permutations of the input string
    """
    result = []  # List to store the permutations
    slate = []  # Temporary list to store the current permutation
    
    def helper(i):
        """
        Recursive helper function to generate letter case permutations
        
        Args:
         i(int): Index of the character to decide on
        """
        if i == len(s):
            result.append("".join(slate))  # Add the current permutation to the result list
            return
        else:
            if s[i].isdigit():
                slate.append(s[i])  # If it is a digit, add it to the current permutation
                helper(i+1)  # Move to the next character
                slate.pop()  # Remove the digit from the current permutation
            else:
                slate.append(s[i].upper())  # Add the uppercase version of the character to the current permutation
                helper(i+1)  # Move to the next character
                slate.pop()  # Remove the uppercase character from the current permutation
                
                slate.append(s[i].lower())  # Add the lowercase version of the character to the current permutation
                helper(i+1)  # Move to the next character
                slate.pop()  # Remove the lowercase character from the current permutation
    
    helper(0)  # Start the recursion from the first character of the input string
    return result  # Return the list of letter case permutations


# Another approach is to use a string slate to store the current permutation. This avoids creating new strings on every recursive call and eliminates the need to store all permutations at once.
# Instead of creating a new string slate at every step in the recursion, you can modify the string in-place using a list. This avoids building new strings on every recursive call. Additionally, you can avoid storing all permutations at once by yielding results one at a time using a generator.
# This approach reduces auxiliary space by removing the need for constructing new strings at each recursive level and eliminates the need to store all results in memory simultaneously.
# Here’s how you could implement it:
# this is often can do with permutations problem, but not in combination problem.

def letter_case_permutations_mutation_2(s):
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
