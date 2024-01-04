from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        ans = []
        window = Counter(s[:k]) 
        n = len(s)

        if window == Counter(p): 
            ans.append(0)
        for i in range(1, n - k + 1):
            
            window[s[i + k - 1]] += 1  
            window[s[i - 1]] -= 1 
            if window == Counter(p):
                ans.append(i)

        return ans
        