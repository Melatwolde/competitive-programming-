
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {}
        

        for idx, num in enumerate(nums):
            d[num] = idx
            print(d[num])
            
        
        for src, dst in operations:
           
            idx = d[src]
            print(idx)
            nums[idx] = dst
            d[dst] = idx
        
        return nums
        
            
        