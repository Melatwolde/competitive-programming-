class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res=[]
        l=0
        while l < len (nums):
            if nums[l]==target:
                res.append(l)
            l+=1
        return res
        
