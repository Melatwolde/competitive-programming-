class Solution:
    def maxCoins(self, piles):
        piles.sort()
        j = len(piles) - 1
        ans = 0
        for i in range(len(piles) // 3):
            j -= 1
            ans += piles[j]
            j -= 1
        return ans

# def divide_into_three_arrays(arr):
#     n = len(arr)
#     third = n // 3
#     subarrays = []
#     for i in range(0, n, third):
#         subarray = arr[i:i+third]
#         subarrays.append(subarray)
#     return subarrays