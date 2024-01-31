class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        n = len(mat)
        # left = 0
        # right = 0
        res = 0
        for i in range(n):
            res += mat[i][i]
            res += mat[i][col - i - 1]
        return res - (mat[n//2][n//2] if n%2 else 0)