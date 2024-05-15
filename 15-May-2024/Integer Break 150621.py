# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [0]*(n+1)
        memo[1] =1
        def dp(n):
            # if n <= 2:
            #     return 1
            if memo[n] != 0:
                return memo[n]
            mem= 0
            for i in range(1,n):
                mem= max(mem, max(i * (n - i), i * dp(n - i)))
            memo[n] =mem
            return mem
        dp(n)
        return memo[n]