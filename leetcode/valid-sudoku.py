class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False
        for row in board:
            temp = [i for i in row if i != '.']
            if len(set(temp)) != len(temp):
                return False

        transpose_dict = defaultdict(list)
        for row in board:
            for i in range(len(row)):
                if row[i] != '.':
                    transpose_dict[i].append(row[i])
        for k, v in transpose_dict.items():
            if len(v) != len(set(v)):
                return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                box = []
                for k in range(i, i + 3):
                    box.extend(board[k][j:j + 3])

                box = [element for element in box if element != '.']
                if len(box) != len(set(box)):
                    return False
        return True


                    # row.add(r)
                    # col.add(c)
                    # subbox.add(b)
                    
                    
        return True

        # row , col = len(board) , len(board[0])
        # for i in range(1, 9):
        #     for j in range(1,9):
        #         if board[i][j] != ".":





        
