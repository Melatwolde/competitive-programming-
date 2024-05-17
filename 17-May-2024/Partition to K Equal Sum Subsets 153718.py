# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        visited = [0] * len(nums)
        return self.dfs(nums, visited, 0, k, 0, target)

    def dfs(self, nums, visited, start_index, k, current_sum, target):
        if k == 1:
            return True
        if current_sum == target:
            return self.dfs(nums, visited, 0, k-1, 0, target)
        for i in range(start_index, len(nums)):
            if visited[i] == 0 and current_sum + nums[i] <= target:
                visited[i] = 1
                if self.dfs(nums, visited, i+1, k, current_sum + nums[i], target):
                    return True
                visited[i] = 0
        return False