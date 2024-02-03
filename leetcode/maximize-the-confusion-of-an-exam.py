class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_consecutive_t = 0
        window_start = 0
        counts = {}
        max_count = 0

        for window_end in range(len(answerKey)):
            right_char = answerKey[window_end]
            counts[right_char] = counts.get(right_char, 0) + 1
            max_count = max(max_count, counts[right_char])

            if (window_end - window_start + 1 - max_count) > k:
                left_char = answerKey[window_start]
                counts[left_char] -= 1
                window_start += 1

            max_consecutive_t = max(max_consecutive_t, window_end - window_start + 1)

        return max_consecutive_t