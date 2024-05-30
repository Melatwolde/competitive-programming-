# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        n = len(quiet)
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        answer = [-1] * n
        
        def dfs(node):
            if answer[node] != -1:
                return answer[node]
            answer[node] = node
            for neighbor in graph[node]:
                candidate = dfs(neighbor)
                if quiet[candidate] < quiet[answer[node]]:
                    answer[node] = candidate
            
            return answer[node]
        
        for i in range(n):
            dfs(i)
        
        return answer

