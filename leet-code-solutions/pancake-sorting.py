class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)
        
        while n > 1:
            
            max_idx = arr.index(max(arr[:n]))
            
            arr[:max_idx+1] = arr[:max_idx+1][::-1]
            flips.append(max_idx+1)
            arr[:n] = arr[:n][::-1]
            flips.append(n)
            
            n -= 1
        
        return flips
