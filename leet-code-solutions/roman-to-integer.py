class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = roman_to_int[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            value_one = roman_to_int[s[i]]
            value_two = roman_to_int[s[i + 1]]
            if value_one < value_two:
                result -= value_one
            else:
                result += value_one

        return result


