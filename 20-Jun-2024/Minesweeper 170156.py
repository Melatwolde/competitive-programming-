# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows = len(board)
        cols = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                    (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def countAdjacentMines(r, c):
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
            return count

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'E':
                return
            adjacentMines = countAdjacentMines(r, c)
            if adjacentMines > 0:
                board[r][c] = str(adjacentMines)
            else:
                board[r][c] = 'B'
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        click_r, click_c = click
        if board[click_r][click_c] == 'M':
            board[click_r][click_c] = 'X'
        else:
            dfs(click_r, click_c)

        return board