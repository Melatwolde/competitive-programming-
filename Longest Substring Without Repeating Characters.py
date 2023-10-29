class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_length = 0
        start = 0
        char_map = {}

        for end in range(len(s)):
            if s[end] in char_map and start <= char_map[s[end]]:
                start = char_map[s[end]] + 1
            else:
                max_length = max(max_length, end - start + 1)

            char_map[s[end]] = end

        return max_length
