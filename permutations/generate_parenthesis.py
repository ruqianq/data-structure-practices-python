class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def helper(num_left, num_right, slate):
            if num_left == 0 and num_right == 0:
                result.append(slate[:])
                return
            if num_right < num_left:
                return
            # adding "("
            if num_left > 0:
                #slate.append("(")
                helper(num_left - 1, num_right, slate + "(")
                #slate.pop()
            if num_right > 0:
                #slate.append(")")
                helper(num_left, num_right - 1, slate + ")")
                #slate.pop()
        helper(n, n, "")
        return result