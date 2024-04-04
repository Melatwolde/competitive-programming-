class Solution:
    def smallestValue(self, n: int) -> int:
        def helper(k):
            factors = []
            while k % 2 == 0:
                factors.append(2)
                k = k // 2
            i = 3
            while i * i <= k:
                while k % i == 0:
                    factors.append(i)
                    k = k // i
                i += 2
            if k > 2:
                factors.append(k)
            return sum(factors)

        k = 2
        while True:
            if helper(k) == n:
                return k
            k += 1