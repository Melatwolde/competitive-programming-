class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for divisor in [2, 3, 5]:
            while n % divisor == 0:
                n //= divisor

        return n == 1