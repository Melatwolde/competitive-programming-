class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.helper(1, n, k, [], ans)
        return ans
    
    def helper(self, start, n, k, sub, ans):
        if k == 0:
            ans.append(sub[:])
            return
        for i in range(start, n - k + 2):
            sub.append(i)
            self.helper(i + 1, n, k - 1, sub, ans)
            sub.pop()
