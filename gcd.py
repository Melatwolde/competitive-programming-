from collections import defaultdict
from typing import List


def hasGroupsSizeX(self, deck: List[int]) -> bool:
    count = defaultdict()
    for i in deck:
        count[i] += 1

    for val, key in count:
        if len(deck) % key != 0:
            return False
    return True

from collections import defaultdict
from typing import List

def hasGroupsSizeX(deck: List[int]) -> bool:
    count = defaultdict(int)
    for i in deck:
        count[i] += 1

    for key, val in count.items():
        if len(deck) % val != 0:
            return False
    return True