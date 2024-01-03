class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i ,j=0, len(people)-1
        c=0
        people.sort()
        
        while(i<=j):
            if people[i]+people[j]<=limit:
                c+=1
                i+=1
                j-=1
            elif people[j]<=limit:
                c+=1
                j-=1
        return c