class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(s):
            if len(s) <= 1:
                return ""

            a_set = set(s)

            for i, c in enumerate(s):
                if c.swapcase() not in a_set:
                    s1 = helper(s[:i])
                    s2 = helper(s[i+1:])
                    return s2 if len(s1) < len(s2) else s1

            return s

        return helper(s)