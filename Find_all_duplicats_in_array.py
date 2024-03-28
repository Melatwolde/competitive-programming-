class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i, res = 0, []
        while i < len(nums):
            new_ = nums[i] -1
            if nums[i]!= nums[new_]:
                nums[i],nums[new_] = nums[new_], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i]) 
        return res
