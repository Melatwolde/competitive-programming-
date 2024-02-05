class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l ,r = 0, 0 
        while l< len(s) and r < len(g):
            if s[l] >= g[r]:
                r+= 1
            l += 1
        return r