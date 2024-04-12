class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4

                    if r > 0 and grid[r-1][c] == 1:  
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:  
                        perimeter -= 2

        return perimeter


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
                return 1
            if grid[r][c] == 2:
                return 0

            grid[r][c] = 2  
            return sum(dfs(r + dr, c + dc) for dr, dc in directions)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)