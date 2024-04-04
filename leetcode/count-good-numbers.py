class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007
        even = pow(5, (n +1) //2, MOD)
        odd = pow(4, n//2, MOD)

        return (even * odd ) % MOD 