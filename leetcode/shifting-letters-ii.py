class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        prefix_array = [0] * (len(s)+1)
        for start, end, direction in shifts:
            counter = 1 if direction == 1 else -1
            prefix_array[start]+=counter
            prefix_array[end+1]-=counter

        for i in range(1, len(prefix_array)):
            prefix_array[i]+=prefix_array[i-1]

        result = ""
        for i in range(len(s)):
            new_val = (ord(s[i]) + prefix_array[i]%26)
            if 97 <= new_val <= 122:
                result+=chr(new_val)
            elif new_val > 122:
                result+=chr(new_val%123 + 97)
            else:
                result+=chr(new_val+26)
        return result
        
#         perfix = [0] * len(s)
#         for shift in shifts:
#             l ,r,m = 0,1,2
#             # for l , r, m in enumrate(shift):

#             for l in shift:
#                 if shift[l] == 0:
                    
#                     perfix[l] -=1
#                     print(perfix)
#                 else:
#                     perfix[l] +=1
#             for r in shift:
#                 if shift[r] == 0:
#                     perfix[r] -=1
#                 else:
#                     perfix[r] +=1
#             for m in shift:
#                 if shift[m] == 0:
#                     perfix[m] -=1
#                 else:
#                     perfix[m] += 1
#         print(perfix)

            

        