class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <=1:
            return ""
        for i in range(len(palindrome)//2):
            if palindrome[i] != "a":
                print(palindrome[i+1:])
                return palindrome[:i] + "a" + palindrome[i+1:] 
        return palindrome[:-1] + "b"
            