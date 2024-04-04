class Solution:
    def sortSentence(self, s: str) -> str:
        s1 = s.split(" ")
        final = [0]*len(s1)

        
        for i in s1:
            final[int(i[-1])-1] = i[:-1]
        return " ".join(final)

        