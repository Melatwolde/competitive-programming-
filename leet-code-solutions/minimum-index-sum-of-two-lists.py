class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict2={}
        lst=[]
        for i in range(len(list2)):
            dict2[list2[i]]=i
        for i in range(len(list1)):
            if list1[i] in dict2:
                lst.append([i+dict2[list1[i]],list1[i]])
        l1=[]
        lst.sort()
        l1.append(lst[0][1])
        for i in range(1,len(lst)):
            if lst[i][0]==lst[i-1][0]:
                l1.append(lst[i][1])
            else:
                break
        return l1
        