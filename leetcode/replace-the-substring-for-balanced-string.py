class Solution:
    def balancedString(self, s: str) -> int:
        remaining_fre = collections.Counter(s)
        res = n = len(s)
        left = 0
        for right, c in enumerate(s):
            remaining_fre[c] -= 1
    
            while left < n and all(remaining_fre[ch] <= n/4 for ch in 'QWER'):
                
                res = min(res, right-left+1)
                remaining_fre[s[left]] += 1 # he goes out of window! into remaining
                left += 1
                
        return res