# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [0] * n 
        longest = -1
        
        def dfs(node, stack):
            nonlocal longest
            if visited[node] == 1: 
                cycle_length = len(stack) - stack.index(node)
                longest = max(longest, cycle_length)
                return
            if visited[node] == 2 or edges[node] == -1:
                return  
            
            visited[node] = 1
            stack.append(node)
            if edges[node] != -1:
                dfs(edges[node], stack)
            stack.pop()
            visited[node] = 2
        
        for i in range(n):
            if visited[i] == 0:
                dfs(i, [])
        
        return longest