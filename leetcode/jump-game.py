class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ = 0
        for i in range(len(nums)):
            if i > max_:
                return False
            max_ = max(max_, i + nums[i])
            if max_ >= len(nums) - 1:
               return True
        return False
        