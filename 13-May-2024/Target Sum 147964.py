# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        tot= sum(nums)
        if tot < abs(target) or (tot + target) % 2 == 1:
            return 0
        sum_val = (tot+ target) // 2
        memo = [0] * (sum_val + 1)
        memo[0] = 1
        for num in nums:
            for i in range(sum_val, num - 1, -1):
                # print(i)
                memo[i] += memo[i - num]
        return memo[sum_val]

