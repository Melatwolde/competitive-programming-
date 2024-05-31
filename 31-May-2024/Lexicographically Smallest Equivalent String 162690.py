# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if rootX < rootY:
                self.parent[rootY] = rootX
            else:
                self.parent[rootX] = rootY

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        
        for a, b in zip(s1, s2):
            uf.union(ord(a) - ord('a'), ord(b) - ord('a'))
        
        result = []
        for ch in baseStr:
            smallest_char = chr(uf.find(ord(ch) - ord('a')) + ord('a'))
            result.append(smallest_char)
        
        return ''.join(result)