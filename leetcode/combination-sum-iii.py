class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans, path = [] , []
        def backtrack(nums,target):
            if target < 0 or len(path) > k:
                return
            if target == 0 and len(path) == k:
                ans.append(path.copy())
                return 
            
            for i in range(nums,10):
                path.append(i)
                backtrack(i+1, target -i)
                path.pop()
        backtrack(1, n)
        return ans
