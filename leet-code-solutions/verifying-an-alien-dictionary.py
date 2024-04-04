class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = dict()
        for i in range(len(order)):
            hashmap[order[i]] = i
        
        score = [[hashmap[i] for i in word] for word in words]
        return sorted(score) == score
        
        