class Solution:
    def minimizedStringLength(self, s: str) -> int:
        freq_s = defaultdict(int)  
        
        for char in s:
            freq_s[char] += 1
        
    
        
        return len(freq_s)

