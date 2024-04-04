class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        start = [0, 0] 
        distance_to_target = abs(target[0] - start[0]) + abs(target[1] - start[1])
        
        for ghost in ghosts:
            ghost_distance_to_target = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if ghost_distance_to_target <= distance_to_target:
                return False

        return True 


