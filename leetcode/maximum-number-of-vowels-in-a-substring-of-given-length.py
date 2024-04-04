class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = " aeiou"
        win = res = 0
        for i in range(len(s)):
            win += s[i] in vowel
            if i >= k:
                win -= s[i-k] in vowel
            res = max(res, win)

        return res