class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split()
        max_length = max(len(word) for word in words)
        result = []
        
        for i in range(max_length):
            vertical_word = ""
            for word in words:
                if i < len(word):
                    vertical_word += word[i]
                else:
                    vertical_word += " "
            result.append(vertical_word.rstrip())
        
        return result