# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        sum_steps = 0
        num_moves = 0
        
        while sum_steps < target or (sum_steps - target) % 2 != 0:
            num_moves += 1
            sum_steps += num_moves
        
        return num_moves