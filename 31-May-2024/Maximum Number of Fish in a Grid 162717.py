# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        self.maxFish = 0
        self.curFish = 0
        self.visit = set()
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if (i,j) in self.visit or grid[i][j] == 0:
                return
            self.curFish += grid[i][j]
            self.maxFish = max(self.curFish, self.maxFish)
            self.visit.add((i,j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                self.curFish = 0
                if grid[x][y] != 0:
                    dfs(x, y)
        
        return self.maxFish