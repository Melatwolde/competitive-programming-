# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
    
        for word in strs:
            sort = ''.join(sorted(word))
            anagrams[sort].append(word)

        return list(anagrams.values())