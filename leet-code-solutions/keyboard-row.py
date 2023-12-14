class Solution:
    def findWords(self, words: List[str]) -> List[str] :
        res = []
        for i in words : 
            if set(i.lower()).issubset(set("qwertyuiop")) | set(i.lower()).issubset(set("asdfghjkl")) | set(i.lower()).issubset(set("zxcvbnm")) : 
                res.append(i) 
        return res