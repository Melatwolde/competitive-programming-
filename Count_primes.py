class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2:
            return 0
        prime = [True] * (n)
        prime[0] = prime[1] = False

        d = 2 
        while d * d <=n:
            if prime[d]:
                for i in range(d * d, n, d):
                    prime[i] = False
            d += 1

        return sum(prime)
