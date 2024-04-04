class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = Counter(s)
        res =0
        odd = 0

        for i in dic.values():
            if i == 1:
                odd+= 1
            new_ = i % 2
            if new_ == 1:
                val = i - new_
                odd += 1
                res += val
            elif i%2 == 0:
                res += i
        if odd > 0:
            res += 1
        return res
        