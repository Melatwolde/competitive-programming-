# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        queue = deque([(0, 0, 1)])
        visited = [[0]*n for _ in range(n)]
        visited[0][0] = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while queue:
            x, y, path_len = queue.popleft()
            if x == y == n - 1:
                return path_len
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny, path_len + 1))
                    visited[nx][ny] = 1

        return -1