class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for i in image:
            i.reverse()
            for num in range(len(i)):
                if i[num] == 0:
                    i[num] = 1
                else:
                    i[num] = 0
        return image