# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        dp = [0] * n
        length = [0] * n

        for i in range(n):
            for ch in words[i]:
                dp[i] |= 1 << (ord(ch) - ord('a'))
            length[i] = len(words[i])

        maxProduct = 0
        for i in range(n):
            for j in range(i+1, n):
                if dp[i] & dp[j] == 0:
                    maxProduct = max(maxProduct, length[i] * length[j])

        return maxProduct