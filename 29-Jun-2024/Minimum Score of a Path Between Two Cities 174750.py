# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))
        
    
        queue = deque([1])
        visited = set()
        min_score = float('inf')
        
        while queue:
            city = queue.popleft()
            if city in visited:
                continue
            visited.add(city)
            
            for neighbor, distance in graph[city]:
                if neighbor not in visited:
                    min_score = min(min_score, distance)
                    queue.append(neighbor)
        
        return min_score