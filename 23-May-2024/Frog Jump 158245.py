# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones):
        if stones[1] != 1:
            return False

        memo = {i: set() for i in stones}
        memo[1].add(1)

        for i in stones[:-1]:
            for j in memo[i]:
                for k in range(j - 1, j + 2):
                    if k > 0 and i + k in memo:
                        memo[i + k].add(k)

        return bool(memo[stones[-1]])