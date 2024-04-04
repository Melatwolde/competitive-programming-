class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination: return 0
        if destination < start: return self.distanceBetweenBusStops(distance, destination, start)
        cwd = 0
        ccwd = 0
        for i in range(len(distance)):
            if start <= i < destination: ccwd += distance[i]
            else: cwd += distance[i]
        return min(cwd, ccwd)


