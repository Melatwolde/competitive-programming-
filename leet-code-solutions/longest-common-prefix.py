class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        prefix = strs[0]  
        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
               
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix