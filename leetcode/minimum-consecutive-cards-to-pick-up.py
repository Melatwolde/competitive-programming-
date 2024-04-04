class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_count = {}
        min_pickup = float('inf')
        
        for i, card in enumerate(cards):
            if card in card_count:
                min_pickup = min(min_pickup, i - card_count[card] + 1)
            card_count[card] = i
        
        return -1 if min_pickup == float('inf') else min_pickup