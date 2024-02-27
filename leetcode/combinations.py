class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def back(nums):
            if len(path) == k:
                ans.append(path.copy())
                return
            for i in range(nums+1, n+1):
                print(i)
                path.append(i)

                back(i)
                path.pop()
        back(0)
        return ans