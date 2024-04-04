class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        stack = []

        for i in salary:
            if i != max(salary) and i != min(salary):
                stack.append(i)

        return sum(stack) / len(stack)