# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    class UnionFind:
        def __init__(self, size):
            self.root = list(range(size))
            self.rank = [1] * size

        def find(self, x):
            if x == self.root[x]:
                return x
            self.root[x] = self.find(self.root[x])  # Path compression
            return self.root[x]

        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)

            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.root[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.root[rootX] = rootY
                else:
                    self.root[rootY] = rootX
                    self.rank[rootX] += 1

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        indexed_queries = sorted([(i, q[0], q[1], q[2]) for i, q in enumerate(queries)], key=lambda x: x[3])

        uf = self.UnionFind(n)
        result = [False] * len(queries)
        edgeIndex = 0

        for i, p, q, limit in indexed_queries:
            while edgeIndex < len(edgeList) and edgeList[edgeIndex][2] < limit:
                uf.union(edgeList[edgeIndex][0], edgeList[edgeIndex][1])
                edgeIndex += 1

            if uf.find(p) == uf.find(q):
                result[i] = True

        return result
