# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        if n <= 1:
            return n
        
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        def similar(x, y):
            diff = 0
            for i in range(len(strs[x])):
                if strs[x][i] != strs[y][i]:
                    diff += 1
            return diff == 2 or diff == 0
        
        for i in range(n):
            for j in range(i+1, n):
                if similar(i, j):
                    union(i, j)
        
        return len(set(find(i) for i in range(n)))
        