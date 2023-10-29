class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_count = {}
        window_count = {}
        for char in s1:
            target_count[char] = target_count.get(char, 0) + 1

        l = 0
        for r in range(len(s2)):
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1

            if r - l + 1 == len(s1):
                if window_count == target_count:
                    return True
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]
                l += 1

        return False

