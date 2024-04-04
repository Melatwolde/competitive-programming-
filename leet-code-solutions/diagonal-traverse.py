from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, column = len(mat), len(mat[0])
        r, c = 0, 0
        stack = []

        for _ in range(row * column):
            stack.append(mat[r][c])

            if (r + c) % 2 == 0:
                if c == column - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == row - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1

        return stack

