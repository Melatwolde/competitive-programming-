class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        d = {}

        for i in range(len(fronts)):
            if fronts[i] != backs[i]:
                if fronts[i] not in d:
                    d[fronts[i]] = True
                if backs[i] not in d:
                    d[backs[i]] = True
            elif fronts[i] == backs[i]:
                d[fronts[i]] = False
        
        new = float('inf')
        for key, value in d.items():
            if value:
                new = min(new, key)
        
        if new != float('inf'):
            return new
        
        return 0
        

        