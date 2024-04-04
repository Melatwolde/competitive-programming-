class Solution:
    def interpret(self, command: str) -> str:
        stack = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                stack += "G"
                i += 1
            elif command[i:i+2] == "()":
                stack += "o"
                i += 2
            elif command[i:i+4] == "(al)":
                stack += "al"
                i += 4
            else:
                stack += command[i]
                i += 1
        return stack


        