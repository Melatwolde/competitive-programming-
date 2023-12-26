class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for i in range(size):
            for j in range (size - i -1):
                if nums[j] > nums[j+1]:
                    nums[j] , nums[j+1] = nums[j+1] ,nums[j]
        