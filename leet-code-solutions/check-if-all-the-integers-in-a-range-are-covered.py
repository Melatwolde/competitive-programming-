class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            covered = False
            for j, k in ranges:
                if j <= i <= k:
                    covered = True
                    break
            if not covered:
                return False
        return True