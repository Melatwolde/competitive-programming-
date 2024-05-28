# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
    
        n = len(s)
        isPalindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            isPalindrome[i][i] = True
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        isPalindrome[i][j] = True
                    else:
                        isPalindrome[i][j] = isPalindrome[i + 1][j - 1]
        
        dp = [0] * n
        for i in range(n):
            if isPalindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = float('inf')
                for j in range(i):
                    if isPalindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[-1]

    
