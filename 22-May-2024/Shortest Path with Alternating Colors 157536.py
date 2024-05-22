# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: defaultdict(list))
        for u, v in redEdges:
            graph[u][0].append(v)
        for u, v in blueEdges:
            graph[u][1].append(v)

        res, visited = [-1] * n, {(0, 0), (0, 1)}
        bfs = deque([(0, 0), (0, 1)]) 

        steps = 0
        while bfs:
            for _ in range(len(bfs)):
                node, color = bfs.popleft()
                if res[node] == -1:
                    res[node] = steps
                for nei in graph[node][color^1]:
                    if (nei, color^1) not in visited:
                        visited.add((nei, color^1))
                        bfs.append((nei, color^1))
            steps += 1

        return [x if x != -1 else -1 for x in res]