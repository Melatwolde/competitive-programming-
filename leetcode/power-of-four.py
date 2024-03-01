class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 4:
            return True
        if n == 1:
            return True
        while n % 4 == 0:
            n = n//4
            if n == 1:
                return True
            
        # for i in range(100):
        #     if (i ** 4) == n:
        #         return True
        
        return False