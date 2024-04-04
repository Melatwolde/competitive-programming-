class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = 0
        for ans, cnt in count.items():
            group_size = ans + 1
            num_groups = (cnt + group_size - 1) // group_size
            res += num_groups * group_size
        return res