# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

class Solution:
    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.rank = [1] * size
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # Path compression
            return self.parent[x]
        
        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1
        
        def can_union(self, x, y, restrictions):
            rootX = self.find(x)
            rootY = self.find(y)
            for r1, r2 in restrictions:
                rootR1 = self.find(r1)
                rootR2 = self.find(r2)
                if (rootX == rootR1 and rootY == rootR2) or (rootX == rootR2 and rootY == rootR1):
                    return False
            return True

    def friendRequests(self, n, restrictions, requests):
        uf = self.UnionFind(n)
        result = []
        
        for u, v in requests:
            if uf.can_union(u, v, restrictions):
                uf.union(u, v)
                result.append(True)
            else:
                result.append(False)
        
        return result
