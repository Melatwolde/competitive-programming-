class UndergroundSystem:

    def __init__(self):
        self.id_time = {}
        self.id_start = {}
        self.travel_time = {}
        self.travel_freq = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_time[id] = t
        self.id_start[id] = stationName
        if stationName not in self.travel_time:
            self.travel_time[stationName] = defaultdict(int)
            self.travel_freq[stationName] = defaultdict(int)
            

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time = t - self.id_time[id]
        start = self.id_start[id]
        end = stationName
        self.travel_time[start][end] += time
        self.travel_freq[start][end] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.travel_time[startStation][endStation] / self.travel_freq[startStation][endStation]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)