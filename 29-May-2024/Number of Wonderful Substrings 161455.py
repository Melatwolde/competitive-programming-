# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask, count = 0, [1] + [0] * 1024
        res = 0
        for ch in word:
            mask ^= 1 << (ord(ch) - ord('a'))
            res += count[mask]
            for i in range(10):
                res += count[mask ^ (1 << i)]
            count[mask] += 1
        return res