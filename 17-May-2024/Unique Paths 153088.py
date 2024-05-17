# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1

        def dpp(i, j):
            if 0 <= i < m and 0 <= j < n:
                return dp[i][j]
            return 0

        for col in range(n - 1, -1, -1):
            for row in range(m - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    continue
                dp[row][col] += dpp(row + 1, col) + dpp(row, col + 1)

        return dp[0][0]