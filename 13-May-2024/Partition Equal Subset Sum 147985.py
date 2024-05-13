# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot= sum(nums)
        if tot % 2 != 0:
            return False
        target = tot // 2
        memo = [False] * (target + 1)
        memo[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                memo[i] = memo[i] or memo[i - num]
        return memo[target]