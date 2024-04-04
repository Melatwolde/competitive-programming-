class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n= len(senate)
        Dire= deque()
        Radiant= deque()

        for i in range (n):
            if senate[i] =='R':
                Radiant.append(i)
            else:
                Dire.append(i)
        while Dire and Radiant:
            r= Radiant.popleft()
            d = Dire.popleft()
            if r<d:
                Radiant.append(r+n)
            else:
                Dire.append(d+n) 
        return "Radiant" if Radiant else "Dire"    
