
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        res = list()
        for direc in paths:
            d = direc.split()
            for i in range(1, len(d)):
                x = d[i].split("(")
                cont = x[1][:-1]
                file_name = d[0] + "/" + x[0]
                contents[cont].append(file_name)
                
        for file in contents:
            if len(contents[file]) > 1:
                res.append(contents[file])
                
        return res
                
            