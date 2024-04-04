class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count_left = 0
        count_right = 0
        for char in s:
            if char == "(":
                count_left += 1
            elif char == ")":
                if count_left > 0:
                    count_left -= 1
                else:
                    count_right += 1
        return count_left + count_right
