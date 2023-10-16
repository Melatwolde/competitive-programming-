from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        q = deque()
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1
        
        dirX = [1, -1, 0, 0]
        dirY = [0, 0, 1, -1]
        
        length = 0
        while q:
            size = len(q)
            length += 1
            for _ in range(size):
                r, c = q.popleft()
                for i in range(4):
                    newRow = r + dirX[i]
                    newCol = c + dirY[i]
                    if 0 <= newRow < rows and 0 <= newCol < cols and mat[newRow][newCol] < 0:
                        mat[newRow][newCol] = length
                        q.append((newRow, newCol))
        
        return mat
