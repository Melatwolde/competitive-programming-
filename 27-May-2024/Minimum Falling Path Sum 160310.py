# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(dp[i-1][j-1] if j > 0 else float('inf'),  dp[i-1][j], dp[i-1][j+1] if j < n-1 else float('inf'))

        return min(dp[-1])