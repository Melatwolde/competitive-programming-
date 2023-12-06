class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)

        x, y = 0, 0
        answer = {}
        answer = []

        while True:

            flag = False
            # print(answer)
            flag1 = False
            while y < right :
                flag = True
                flag1 = True
                answer.append(matrix[x][y])
                y += 1
            
            right -= 1
            y -= 1
            x += 1
            flag2 = False
            while x < bottom and flag1:
                flag = True
                flag2 = True
                answer.append(matrix[x][y])
                x += 1
            bottom -= 1
            x -= 1
            y -= 1
            flag3 = False
            while y >= left and flag2:
                flag = True
                flag3 = True
                answer.append(matrix[x][y])
                y -= 1
            left += 1
            y += 1
            x -= 1

            flag4 = True
            while x > top and flag3:
                flag = True
                flag4 = False
                answer.append(matrix[x][y])
                x -= 1
            
            if flag4:
                return answer

            top += 1
            x += 1
            y += 1

