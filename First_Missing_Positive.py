class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  
            else:
                i += 1

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1

        return len(nums) + 1