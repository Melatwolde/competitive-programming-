# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        for i in range(len(nums)):
            num = str(nums[i])
            form = ""
            for j in range(len(num)):
                form += str(mapping[int(num[j])])
            mapped_value = int(form)
            pairs.append((mapped_value,i))
        
        pairs.sort()
        answer = []
        for pair in pairs:
            answer.append(nums[pair[1]])
        return answer