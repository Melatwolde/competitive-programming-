class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        stack = []
        longest_streak = 1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

           
            if stack and nums[i] == stack[-1] + 1:
                stack.append(nums[i])
            else:
                # Start a new streak
                stack = [nums[i]]

            longest_streak = max(longest_streak, len(stack))

        return longest_streak  
               