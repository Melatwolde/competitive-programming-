class Solution:
    def isUgly(self, n: int) -> bool:
        # if n <= 0:
        #     return False

        # factors, val  = [], [2,3,5]
        # divisor = 2

        # while divisor <= n:
        #     if n % divisor == 0:
        #         factors.append(divisor)
        #         n //= divisor
        #     else:
        #         divisor += 1

        # for i in factors:
        #     if i not in val:
        #         return False
        # return True
        if n <= 0:
            return False

        for divisor in [2, 3, 5]:
            while n % divisor == 0:
                n //= divisor

        return n == 1