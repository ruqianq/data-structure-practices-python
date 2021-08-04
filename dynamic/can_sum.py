# You are given an integer array nums and an integer target.
#
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and
# then concatenate all the integers.
#
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the
# expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# this is can sum problem to find out all the possible paths (sum) to get to target
# create a grid with len(nums) * len(nums)
# 0/1 Knapsack

def find_target_sum_ways(nums, S):
    index = len(nums) - 1
    curr_sum = 0
    memo = {}

    def dp(nums, target, index, curr_sum):

        if (index, curr_sum) in memo:
            return memo[(index, curr_sum)]

        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0

        positive = dp(nums, target, index-1, curr_sum + nums[index])
        negative = dp(nums, target, index-1, curr_sum + -nums[index])

        memo[(index, curr_sum)] = positive + negative
        return memo[(index, curr_sum)]
    return dp(nums, S, index, curr_sum)
