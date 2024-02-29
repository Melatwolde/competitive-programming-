class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()
        def backtrack(nums):
            if sum(path) >= target:
                if sum(path) == target and path not in ans:
                    ans.append(path.copy())
                return


            for i in range(nums, len(candidates)):
                if i > nums and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return ans