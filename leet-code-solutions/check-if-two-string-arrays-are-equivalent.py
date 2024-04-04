class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        res1 = ''.join(word1)
        res2 = ''.join(word2)
        return res1 == res2