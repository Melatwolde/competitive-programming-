class Solution:
    def maxScore(self, s: str) -> int:
       
        
        maxScore = 0
        n = len(s)
        
        for i in range(1, n):
            left = s[:i]
            right = s[i:]
            score = left.count('0') + right.count('1')
            maxScore = max(maxScore, score)
        
        return maxScore