class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = set()
        lose = set()
        rest = set()

        for [winner, loser] in matches:
            if loser in win:
                lose.add(loser)
                win.remove(loser)

            elif loser in lose:
                rest.add(loser)
                lose.remove(loser)

            elif loser not in rest:
                lose.add(loser)
            
            if winner not in rest and winner not in lose:
                win.add(winner)

        return [sorted(list(win)), sorted(list(lose))]