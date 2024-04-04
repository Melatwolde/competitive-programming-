class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        if len(s) <= 1:
            return True

        s = s.lower()
        s_list = []

        for char in s:
            if char.isalnum():
                s_list.append(char)
            else:
                continue

        i = 0
        j = len(s_list) - 1 

        while i <= j:
            if s_list[i] != s_list[j]:
                
                return False
            
            i += 1
            j -= 1
        
        return True