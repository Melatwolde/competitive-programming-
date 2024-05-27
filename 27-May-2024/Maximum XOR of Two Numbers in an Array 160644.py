# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}
        for num in nums:
            node = root
            for bit in range(31, -1, -1):
                bit_val = (num >> bit) & 1
                if bit_val not in node:
                    node[bit_val] = {}
                node = node[bit_val]
            node['firststar'] = num


        max_xor = 0
        for num in nums:
            node = root
            curr_xor = 0
            for bit in range(31, -1, -1):
                bit_val = (num >> bit) & 1
                if 1 - bit_val in node:
                    curr_xor |= (1 << bit)
                    node = node[1 - bit_val]
                else:
                    node = node[bit_val]
            max_xor = max(max_xor, curr_xor)

        return max_xor