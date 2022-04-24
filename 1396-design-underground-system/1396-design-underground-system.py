# Nice Qsn , applying concept to rl scenario
# startStation+str(len(startStation))+endStation+str(len(endStation)) : to create a unique key for eact start-end station pair .. to pass 'a','aa','b','ab' as station names
class UndergroundSystem:

    def __init__(self):
        self.ppl=defaultdict(list)
        self.stationtime=defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ppl[id]=[] # ensure old values are not reused in checkOut , as passenger does >1 travels
        self.ppl[id].append(stationName)
        self.ppl[id].append(t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.ppl[id].append(stationName)
        self.ppl[id].append(t)
        self.stationtime[self.ppl[id][0]+str(len(self.ppl[id][0]))+self.ppl[id][2]+str(len(self.ppl[id][2]))].append(self.ppl[id][3] - self.ppl[id][1]) #create unique stationfromto name , append time difference to this  list in defaultdict(list)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        l=self.stationtime[startStation+str(len(startStation))+endStation+str(len(endStation))]
        return(sum(l)/len(l)) #calc avg
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)