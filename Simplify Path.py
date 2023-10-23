class Solution:
    def simplifyPath(self, path):
        stack = []
        path = path.split("/")
        for elem in path:
            if stack and elem == "..":
                stack.pop()
            elif elem not in [".", "", ".."]:
                stack.append(elem)
                
        return "/" + "/".join(stack)
