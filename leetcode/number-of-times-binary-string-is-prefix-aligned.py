class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        l = 1e9
        r , res = 0 , 0
        flipone = False
        for i in range(n):
            if flips[i] < l:
                l = flips[i]
            if flips[i] > r:
                r = flips[i]
            if r == i + 1:
                flipone = True
            if flipone and r == i + 1:
                res += 1
        return res

        


                