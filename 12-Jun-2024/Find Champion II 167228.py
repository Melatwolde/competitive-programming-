# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        set_ =set()
        for i in range(n):
            set_.add(i)
        for j in edges:
            set_.discard(j[1])
        if len(set_)>1:
            return -1
        for i in set_:
            return i