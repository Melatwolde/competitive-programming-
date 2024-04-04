class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # mods = {i : 0 for i in range(len(arr))}
        mods = defaultdict(int)


        for i  in arr:
            mods[i%k] += 1
        if mods[0]%2 != 0:
            return False
        for mod in mods:
            if mods[mod] != mods[(k - mod)%k]:
                return False
        return True