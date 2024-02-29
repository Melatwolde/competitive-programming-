class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        path = []
        nums.sort()
        
        def backtrack(start):
            subsets.append(path.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue  
                
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return subsets