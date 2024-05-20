# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [-1]*(target+1)
        memo[0] = 1 
        def dp(target):
            if target < 0: 
                return 0
            if memo[target] != -1: 
                return memo[target]
            res = 0
            for num in nums:
                res += dp(target - num)
            memo[target] = res 
            return res

        return dp(target)