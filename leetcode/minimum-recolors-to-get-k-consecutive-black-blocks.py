class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if blocks.count('b') == k:
            return 0
        
        num_whites = sum(1 for block in blocks[:k] if block == 'W')
        min_ops = num_whites

        for i in range(1, len(blocks) - k + 1):
            if blocks[i - 1] == 'W':
                num_whites -= 1
            if blocks[i + k - 1] == 'W':
                num_whites += 1
            min_ops = min(min_ops, num_whites)

        return min_ops
